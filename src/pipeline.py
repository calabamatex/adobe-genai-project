"""Main pipeline orchestrator for creative automation."""
import asyncio
import time
import psutil
import platform
from pathlib import Path
from typing import Optional, List, Dict
from datetime import datetime

from src.models import (
    CampaignBrief,
    ComprehensiveBrandGuidelines,
    LocalizationGuidelines,
    LegalComplianceGuidelines,
    CampaignMessage,
    GeneratedAsset,
    CampaignOutput,
    TechnicalMetrics,
    BusinessMetrics
)
from src.genai.factory import ImageGenerationFactory
from src.genai.claude import ClaudeService
from src.parsers.brand_parser import BrandGuidelinesParser
from src.parsers.localization_parser import LocalizationGuidelinesParser
from src.parsers.legal_parser import LegalComplianceParser
from src.image_processor_v2 import ImageProcessorV2 as ImageProcessor
from src.legal_checker import LegalComplianceChecker
from src.storage import StorageManager


class CreativeAutomationPipeline:
    """Main pipeline orchestrator."""

    def __init__(self, image_backend: str = None):
        """
        Initialize pipeline with specified image generation backend.

        Args:
            image_backend: Backend to use ('firefly', 'openai', 'gemini').
                          If None, uses brief's backend or config default.
        """
        self.default_image_backend = image_backend
        self.image_service = None  # Will be created based on campaign brief
        self.claude_service = ClaudeService()
        self.brand_parser = BrandGuidelinesParser(self.claude_service)
        self.locale_parser = LocalizationGuidelinesParser(self.claude_service)
        self.legal_parser = LegalComplianceParser(self.claude_service)
        self.image_processor = ImageProcessor()
        self.storage = StorageManager()
    
    async def process_campaign(
        self,
        brief: CampaignBrief,
        brief_path: Optional[str] = None
    ) -> CampaignOutput:
        """
        Process complete campaign and generate all assets.

        Args:
            brief: Campaign brief with product and localization info
            brief_path: Optional path to brief file for backup/update

        Returns:
            CampaignOutput with generated assets and metrics
        """
        start_time = time.time()

        # Initialize metric tracking
        api_response_times = []
        cache_hits = 0
        cache_misses = 0
        retry_count = 0
        retry_reasons = []
        full_error_traces = []
        total_api_calls = 0
        image_processing_start = 0
        image_processing_total_ms = 0.0
        localization_total_ms = 0.0
        compliance_check_start = 0
        compliance_check_total_ms = 0.0
        process = psutil.Process()
        initial_memory_mb = process.memory_info().rss / (1024 * 1024)
        peak_memory_mb = initial_memory_mb

        # Backup original brief if path provided
        if brief_path:
            try:
                backup_path = self.storage.backup_campaign_brief(brief_path)
                print(f"📋 Backed up original brief to: {backup_path}")
            except Exception as e:
                print(f"⚠️  Could not backup brief: {e}")
                # Continue processing even if backup fails

        # Initialize image generation service based on brief or default
        backend = self.default_image_backend or brief.image_generation_backend
        try:
            self.image_service = ImageGenerationFactory.create(backend)
            backend_name = self.image_service.get_backend_name()
        except Exception as e:
            print(f"❌ Error initializing backend '{backend}': {e}")
            raise

        print(f"\n🚀 Processing Campaign: {brief.campaign_name}")
        print(f"Campaign ID: {brief.campaign_id}")
        print(f"Image Backend: {backend_name}")
        print(f"Products: {len(brief.products)}")
        print(f"Target Locales: {', '.join(brief.target_locales)}")

        # Note: Output directories created automatically when assets are saved
        
        # Load external guidelines
        brand_guidelines = None
        localization_guidelines = None
        legal_guidelines = None

        if brief.brand_guidelines_file:
            print(f"\n📋 Loading brand guidelines from {brief.brand_guidelines_file}...")
            try:
                brand_guidelines = await self.brand_parser.parse(brief.brand_guidelines_file)
                print("✓ Brand guidelines loaded")
            except Exception as e:
                print(f"⚠️  Error loading brand guidelines: {e}")

        if brief.enable_localization and brief.localization_guidelines_file:
            print(f"\n🌍 Loading localization guidelines from {brief.localization_guidelines_file}...")
            try:
                localization_guidelines = await self.locale_parser.parse(brief.localization_guidelines_file)
                print("✓ Localization guidelines loaded")
            except Exception as e:
                print(f"⚠️  Error loading localization guidelines: {e}")

        if brief.legal_compliance_file:
            print(f"\n⚖️  Loading legal compliance guidelines from {brief.legal_compliance_file}...")
            try:
                legal_guidelines = await self.legal_parser.parse(brief.legal_compliance_file)
                print("✓ Legal compliance guidelines loaded")

                # Run compliance check on campaign content
                print(f"\n⚖️  Checking legal compliance...")
                compliance_check_start = time.time()
                checker = LegalComplianceChecker(legal_guidelines)

                # Check campaign message
                is_compliant, violations = checker.check_content(
                    brief.campaign_message,
                    product_content=None,
                    locale=brief.target_locales[0] if brief.target_locales else "en-US"
                )

                # Check each product
                for product in brief.products:
                    product_content = {
                        "description": product.product_description,
                        "features": product.key_features
                    }
                    product_compliant, product_violations = checker.check_content(
                        brief.campaign_message,
                        product_content=product_content,
                        locale=brief.target_locales[0] if brief.target_locales else "en-US"
                    )

                    if not product_compliant:
                        is_compliant = False

                # Display compliance report
                if violations:
                    print("\n" + checker.generate_report())

                    # Check if there are blocking errors
                    summary = checker.get_violation_summary()
                    if summary["errors"] > 0:
                        print(f"\n❌ Campaign cannot proceed due to {summary['errors']} legal compliance error(s)")
                        print("   Please fix the errors above and try again.")
                        raise Exception("Legal compliance check failed - errors must be resolved")
                    elif summary["warnings"] > 0:
                        print(f"\n⚠️  Campaign can proceed but {summary['warnings']} warning(s) should be reviewed")
                else:
                    print("✓ No legal compliance violations found")

                # Track compliance check time
                compliance_check_total_ms = (time.time() - compliance_check_start) * 1000

            except FileNotFoundError as e:
                print(f"⚠️  Error loading legal guidelines: {e}")
            except Exception as e:
                if "Legal compliance check failed" in str(e):
                    raise  # Re-raise compliance errors
                print(f"⚠️  Error during legal compliance check: {e}")
        
        # Process products concurrently
        print(f"\n🎨 Generating assets for {len(brief.products)} products...")

        generated_assets: List[GeneratedAsset] = []
        hero_images: Dict[str, str] = {}  # Track hero images for brief update
        errors = []

        # Process each product
        for product in brief.products:
            print(f"\n📦 Processing product: {product.product_name} ({product.product_id})")
            
            try:
                hero_image_saved = False
                hero_image_path = None

                # Generate or load hero image
                if product.existing_assets and 'hero' in product.existing_assets:
                    print(f"  ✓ Using existing hero image: {product.existing_assets['hero']}")
                    try:
                        with open(product.existing_assets['hero'], 'rb') as f:
                            hero_image_bytes = f.read()
                        hero_image_path = product.existing_assets['hero']
                        hero_image_saved = True
                        cache_hits += 1  # Track cache hit
                    except (FileNotFoundError, IOError) as e:
                        print(f"  ⚠️  Could not read existing image: {e}")
                        print(f"  🎨 Generating hero image instead with {backend_name}...")
                        prompt = product.generation_prompt or f"professional product photo of {product.product_name}, {product.product_description}"

                        # Track API call timing
                        api_start = time.time()
                        hero_image_bytes = await self.image_service.generate_image(
                            prompt,
                            size="2048x2048",
                            brand_guidelines=brand_guidelines
                        )
                        api_response_time_ms = (time.time() - api_start) * 1000
                        api_response_times.append(api_response_time_ms)
                        total_api_calls += 1
                        cache_misses += 1  # Track cache miss
                else:
                    print(f"  🎨 Generating hero image with {backend_name}...")
                    prompt = product.generation_prompt or f"professional product photo of {product.product_name}, {product.product_description}"

                    # Track API call timing
                    api_start = time.time()
                    hero_image_bytes = await self.image_service.generate_image(
                        prompt,
                        size="2048x2048",
                        brand_guidelines=brand_guidelines
                    )
                    api_response_time_ms = (time.time() - api_start) * 1000
                    api_response_times.append(api_response_time_ms)
                    total_api_calls += 1
                    cache_misses += 1  # Track cache miss
                    print(f"  ✓ Hero image generated")

                    # Save generated hero image for future reuse
                    hero_dir = self.storage.output_dir / product.product_id / brief.campaign_id / "hero"
                    hero_dir.mkdir(parents=True, exist_ok=True)
                    hero_image_path = str(hero_dir / f"{product.product_id}_hero.png")

                    # Convert bytes to PIL Image and save
                    from PIL import Image
                    from io import BytesIO
                    hero_img = Image.open(BytesIO(hero_image_bytes))
                    hero_img.save(hero_image_path, optimize=True, quality=95)
                    hero_image_saved = True
                    print(f"  💾 Saved hero image: {hero_image_path}")
                
                # Process each locale
                for locale in brief.target_locales:
                    print(f"\n  🌍 Processing locale: {locale}")

                    # Localize message (only if needed)
                    if locale != brief.campaign_message.locale and localization_guidelines:
                        loc_start = time.time()
                        localized_message = await self.claude_service.localize_message(
                            brief.campaign_message,
                            locale,
                            localization_guidelines
                        )
                        localization_total_ms += (time.time() - loc_start) * 1000
                    else:
                        localized_message = brief.campaign_message

                    # Generate variations for each aspect ratio
                    for ratio in brief.aspect_ratios:
                        # Check if this specific asset already exists
                        asset_key = f"{locale}_{ratio}"

                        if product.existing_assets and asset_key in product.existing_assets:
                            existing_path = product.existing_assets[asset_key]
                            # Verify the file actually exists
                            if Path(existing_path).exists():
                                print(f"    ✓ Using existing {ratio} asset: {existing_path}")
                                asset_path = Path(existing_path)
                            else:
                                print(f"    ⚠️  Existing asset not found, regenerating {ratio}...")
                                # Generate since file doesn't exist
                                img_proc_start = time.time()

                                resized_image = self.image_processor.resize_to_aspect_ratio(
                                    hero_image_bytes,
                                    ratio
                                )
                                final_image = self.image_processor.apply_text_overlay(
                                    resized_image,
                                    localized_message,
                                    brand_guidelines
                                )

                                # Apply logo overlay if logo asset exists
                                if product.existing_assets and 'logo' in product.existing_assets:
                                    logo_path = product.existing_assets['logo']
                                    if Path(logo_path).exists():
                                        final_image = self.image_processor.apply_logo_overlay(
                                            final_image,
                                            logo_path,
                                            brand_guidelines
                                        )

                                # NEW: Apply post-processing (Phase 1)
                                if brand_guidelines and brand_guidelines.post_processing:
                                    final_image = self.image_processor.apply_post_processing(
                                        final_image,
                                        brand_guidelines.post_processing
                                    )

                                image_processing_total_ms += (time.time() - img_proc_start) * 1000

                                output_format = brief.output_formats[0] if brief.output_formats else "png"
                                asset_path = self.storage.get_asset_path(
                                    brief.campaign_id,
                                    locale,
                                    product.product_id,
                                    ratio,
                                    output_format
                                )
                                self.storage.save_image(final_image, asset_path)
                                print(f"    ✓ Saved: {asset_path}")
                        else:
                            # Asset doesn't exist in brief, generate it
                            print(f"    📐 Generating {ratio} variation...")

                            # Track image processing time
                            img_proc_start = time.time()

                            # Resize image
                            resized_image = self.image_processor.resize_to_aspect_ratio(
                                hero_image_bytes,
                                ratio
                            )

                            # Apply text overlay
                            final_image = self.image_processor.apply_text_overlay(
                                resized_image,
                                localized_message,
                                brand_guidelines
                            )

                            # Apply logo overlay if logo asset exists
                            if product.existing_assets and 'logo' in product.existing_assets:
                                logo_path = product.existing_assets['logo']
                                if Path(logo_path).exists():
                                    final_image = self.image_processor.apply_logo_overlay(
                                        final_image,
                                        logo_path,
                                        brand_guidelines
                                    )

                            # NEW: Apply post-processing (Phase 1)
                            if brand_guidelines and brand_guidelines.post_processing:
                                final_image = self.image_processor.apply_post_processing(
                                    final_image,
                                    brand_guidelines.post_processing
                                )

                            image_processing_total_ms += (time.time() - img_proc_start) * 1000

                            # Save
                            output_format = brief.output_formats[0] if brief.output_formats else "png"
                            asset_path = self.storage.get_asset_path(
                                brief.campaign_id,
                                locale,
                                product.product_id,
                                ratio,
                                output_format
                            )

                            self.storage.save_image(final_image, asset_path)
                            print(f"    ✓ Saved: {asset_path}")

                        # Track asset (whether reused or generated)
                        asset = GeneratedAsset(
                            product_id=product.product_id,
                            locale=locale,
                            aspect_ratio=ratio,
                            file_path=str(asset_path),
                            generation_method=backend,  # Fixed: Use actual backend name
                            timestamp=datetime.now()
                        )
                        generated_assets.append(asset)

                # Track hero image path if saved
                if hero_image_saved and hero_image_path:
                    hero_images[product.product_id] = hero_image_path

            except Exception as e:
                import traceback
                error_msg = f"Error processing product {product.product_id}: {str(e)}"
                print(f"  ❌ {error_msg}")
                errors.append(error_msg)

                # Capture full error trace
                full_error_traces.append({
                    "product_id": product.product_id,
                    "error": str(e),
                    "traceback": traceback.format_exc()
                })

            # Update peak memory usage after each product
            current_memory_mb = process.memory_info().rss / (1024 * 1024)
            peak_memory_mb = max(peak_memory_mb, current_memory_mb)
        
        # Calculate metrics
        elapsed_time = time.time() - start_time
        total_expected = len(brief.products) * len(brief.target_locales) * len(brief.aspect_ratios)
        success_rate = len(generated_assets) / total_expected if total_expected > 0 else 0.0

        # Calculate technical metrics
        cache_hit_rate = (cache_hits / (cache_hits + cache_misses) * 100) if (cache_hits + cache_misses) > 0 else 0.0
        avg_api_response_time = sum(api_response_times) / len(api_response_times) if api_response_times else 0.0
        min_api_response_time = min(api_response_times) if api_response_times else 0.0
        max_api_response_time = max(api_response_times) if api_response_times else 0.0

        system_info = {
            "platform": platform.system(),
            "platform_version": platform.version(),
            "python_version": platform.python_version(),
            "processor": platform.processor(),
            "machine": platform.machine()
        }

        technical_metrics = TechnicalMetrics(
            backend_used=backend,
            total_api_calls=total_api_calls,
            cache_hits=cache_hits,
            cache_misses=cache_misses,
            cache_hit_rate=cache_hit_rate,
            retry_count=retry_count,
            retry_reasons=retry_reasons,
            avg_api_response_time_ms=avg_api_response_time,
            min_api_response_time_ms=min_api_response_time,
            max_api_response_time_ms=max_api_response_time,
            image_processing_time_ms=image_processing_total_ms,
            localization_time_ms=localization_total_ms,
            compliance_check_time_ms=compliance_check_total_ms,
            peak_memory_mb=peak_memory_mb,
            system_info=system_info,
            full_error_traces=full_error_traces
        )

        # Calculate business metrics
        # Baseline assumptions: Manual process = 3-5 days (96 hours avg), $2,700 for 36 assets
        manual_baseline_hours = 96.0  # 4 days average
        manual_baseline_cost = 2700.0  # For 36 assets
        avg_hourly_rate = 50.0

        elapsed_hours = elapsed_time / 3600
        time_saved_hours = manual_baseline_hours - elapsed_hours
        time_saved_percentage = (time_saved_hours / manual_baseline_hours * 100) if manual_baseline_hours > 0 else 0.0

        # Estimate manual cost for this campaign (scale from 36-asset baseline)
        estimated_manual_cost = manual_baseline_cost * (total_expected / 36.0)

        # Typical cost savings: 70-90% (use 80% average, adjusted by cache hit rate)
        cache_savings_bonus = cache_hit_rate / 100 * 0.15  # Up to 15% bonus for high cache utilization
        cost_savings_percentage = min(80.0 + (cache_savings_bonus * 100), 95.0)

        estimated_savings = estimated_manual_cost * (cost_savings_percentage / 100)
        actual_cost_estimate = estimated_manual_cost - estimated_savings
        roi_multiplier = estimated_savings / actual_cost_estimate if actual_cost_estimate > 0 else 0.0

        labor_hours_saved = time_saved_hours

        # Compliance pass rate (percentage of products that passed compliance)
        compliant_products = len([p for p in brief.products]) - len([e for e in errors if "compliance" in e.lower()])
        compliance_pass_rate = (compliant_products / len(brief.products) * 100) if brief.products else 100.0

        # Asset reuse efficiency (same as cache hit rate)
        asset_reuse_efficiency = cache_hit_rate

        # Localization efficiency
        num_locales = len(brief.target_locales)
        avg_time_per_locale_seconds = elapsed_time / num_locales if num_locales > 0 else 0.0
        avg_time_per_asset_seconds = elapsed_time / len(generated_assets) if generated_assets else 0.0
        assets_per_hour = (len(generated_assets) / elapsed_hours) if elapsed_hours > 0 else 0.0

        business_metrics = BusinessMetrics(
            time_saved_vs_manual_hours=time_saved_hours,
            time_saved_percentage=time_saved_percentage,
            cost_savings_percentage=cost_savings_percentage,
            manual_baseline_cost=manual_baseline_cost,
            estimated_manual_cost=estimated_manual_cost,
            estimated_savings=estimated_savings,
            roi_multiplier=roi_multiplier,
            labor_hours_saved=labor_hours_saved,
            compliance_pass_rate=compliance_pass_rate,
            asset_reuse_efficiency=asset_reuse_efficiency,
            avg_time_per_locale_seconds=avg_time_per_locale_seconds,
            avg_time_per_asset_seconds=avg_time_per_asset_seconds,
            localization_efficiency_score=assets_per_hour
        )

        # Create output summary
        output = CampaignOutput(
            campaign_id=brief.campaign_id,
            campaign_name=brief.campaign_name,
            generated_assets=generated_assets,
            total_assets=len(generated_assets),
            locales_processed=brief.target_locales,
            products_processed=[p.product_id for p in brief.products],
            processing_time_seconds=elapsed_time,
            success_rate=success_rate,
            errors=errors,
            generation_timestamp=datetime.now(),
            technical_metrics=technical_metrics,
            business_metrics=business_metrics
        )

        # Save per-product reports
        report_paths = []
        for product in brief.products:
            report_path = self.storage.save_report(
                output,
                brief.campaign_id,
                product.product_id
            )
            report_paths.append(report_path)
            print(f"   📄 Report saved: {report_path}")

        # Update original brief with generated asset paths
        if brief_path:
            try:
                self.storage.update_campaign_brief(brief_path, output, hero_images)
            except Exception as e:
                print(f"⚠️  Could not update brief: {e}")
                # Don't fail the pipeline if update fails

        print(f"\n✅ Campaign processing complete!")
        print(f"   Total assets generated: {len(generated_assets)}")
        print(f"   Processing time: {elapsed_time:.1f} seconds")
        print(f"   Success rate: {success_rate * 100:.1f}%")
        print(f"   Reports saved: {len(report_paths)} product reports")

        # Display enhanced metrics
        print(f"\n📊 Technical Metrics:")
        print(f"   Backend: {backend}")
        print(f"   API Calls: {total_api_calls} total, {cache_hits} cache hits ({cache_hit_rate:.1f}% hit rate)")
        print(f"   API Response Time: {avg_api_response_time:.0f}ms avg ({min_api_response_time:.0f}-{max_api_response_time:.0f}ms range)")
        print(f"   Image Processing: {image_processing_total_ms:.0f}ms total")
        print(f"   Localization: {localization_total_ms:.0f}ms total")
        if compliance_check_total_ms > 0:
            print(f"   Compliance Check: {compliance_check_total_ms:.0f}ms")
        print(f"   Peak Memory: {peak_memory_mb:.1f} MB")

        print(f"\n💰 Business Metrics:")
        print(f"   Time Saved: {time_saved_hours:.1f} hours ({time_saved_percentage:.1f}% vs manual)")
        print(f"   Cost Savings: {cost_savings_percentage:.1f}% (Est. ${estimated_savings:,.2f} saved)")
        print(f"   ROI Multiplier: {roi_multiplier:.1f}x")
        print(f"   Asset Reuse Efficiency: {asset_reuse_efficiency:.1f}%")
        print(f"   Localization Efficiency: {assets_per_hour:.1f} assets/hour")
        print(f"   Compliance Pass Rate: {compliance_pass_rate:.1f}%")

        return output
