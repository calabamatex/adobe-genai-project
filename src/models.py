"""
Pydantic data models for Creative Automation Pipeline.
All models use Pydantic v2 for validation and serialization.
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, validator, field_validator
from datetime import datetime
from enum import Enum


class AspectRatio(str, Enum):
    """Supported aspect ratios for campaign assets."""
    SQUARE = "1:1"
    STORY = "9:16"
    LANDSCAPE = "16:9"
    PORTRAIT = "4:5"


class Market(str, Enum):
    """Supported markets/locales."""
    EN_US = "en-US"
    ES_MX = "es-MX"
    FR_CA = "fr-CA"
    PT_BR = "pt-BR"
    DE_DE = "de-DE"
    JA_JP = "ja-JP"
    KO_KR = "ko-KR"


class Product(BaseModel):
    """Product information for campaign asset generation."""
    product_id: str = Field(..., description="Unique product identifier")
    product_name: str = Field(..., description="Product display name")
    product_description: str = Field(..., description="Detailed product description")
    product_category: str = Field(..., description="Product category")
    key_features: List[str] = Field(default_factory=list, description="Key product features")
    existing_assets: Optional[Dict[str, str]] = Field(
        default=None,
        description="Paths to existing assets (hero, logo, etc.)"
    )
    generation_prompt: Optional[str] = Field(
        default=None,
        description="Custom prompt for image generation"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "product_id": "HEADPHONES-001",
                "product_name": "Premium Wireless Headphones",
                "product_description": "High-fidelity wireless headphones with active noise cancellation",
                "product_category": "Electronics",
                "key_features": ["Active Noise Cancellation", "40-hour battery", "Premium audio quality"],
                "generation_prompt": "professional product photo of premium wireless headphones"
            }
        }


class CampaignMessage(BaseModel):
    """Campaign messaging for specific locale."""
    locale: str = Field(default="en-US", description="Target locale code")
    headline: str = Field(..., min_length=1, description="Main headline")
    subheadline: str = Field(..., min_length=1, description="Supporting subheadline")
    cta: str = Field(..., min_length=1, description="Call-to-action text")

    class Config:
        json_schema_extra = {
            "example": {
                "locale": "en-US",
                "headline": "Elevate Your Sound",
                "subheadline": "Experience Premium Audio Quality",
                "cta": "Shop Now"
            }
        }


class TextShadow(BaseModel):
    """Text shadow configuration."""
    enabled: bool = Field(default=True, description="Enable drop shadow")
    color: str = Field(default="#000000", description="Shadow color (hex)")
    offset_x: int = Field(default=2, description="Horizontal offset in pixels")
    offset_y: int = Field(default=2, description="Vertical offset in pixels")
    blur_radius: int = Field(default=0, description="Blur radius in pixels")

    class Config:
        json_schema_extra = {
            "example": {
                "enabled": True,
                "color": "#000000",
                "offset_x": 3,
                "offset_y": 3,
                "blur_radius": 2
            }
        }


class TextOutline(BaseModel):
    """Text outline/stroke configuration."""
    enabled: bool = Field(default=False, description="Enable text outline")
    color: str = Field(default="#FFFFFF", description="Outline color (hex)")
    width: int = Field(default=2, ge=1, le=10, description="Outline width in pixels")

    class Config:
        json_schema_extra = {
            "example": {
                "enabled": True,
                "color": "#FFFFFF",
                "width": 2
            }
        }


class TextBackgroundBox(BaseModel):
    """Text background box configuration."""
    enabled: bool = Field(default=False, description="Enable background box")
    color: str = Field(default="#000000", description="Background color (hex)")
    opacity: float = Field(default=0.7, ge=0.0, le=1.0, description="Opacity (0.0-1.0)")
    padding: int = Field(default=10, ge=0, le=50, description="Padding around text in pixels")

    class Config:
        json_schema_extra = {
            "example": {
                "enabled": True,
                "color": "#000000",
                "opacity": 0.8,
                "padding": 15
            }
        }


class TextElementStyle(BaseModel):
    """Styling for a single text element (headline, subheadline, or CTA)."""
    color: str = Field(default="#FFFFFF", description="Text color (hex)")
    font_size_multiplier: float = Field(default=1.0, ge=0.5, le=3.0, description="Font size multiplier")
    font_weight: str = Field(default="regular", description="Font weight: regular, bold, black")

    # Optional effects
    shadow: Optional[TextShadow] = Field(default=None, description="Drop shadow configuration")
    outline: Optional[TextOutline] = Field(default=None, description="Text outline configuration")
    background: Optional[TextBackgroundBox] = Field(default=None, description="Background box configuration")

    # Positioning
    horizontal_align: str = Field(default="center", description="Horizontal alignment: left, center, right")
    max_width_percentage: float = Field(default=0.90, ge=0.1, le=1.0, description="Max width as percentage of image")

    @field_validator('font_weight')
    def validate_font_weight(cls, v):
        valid_weights = {"regular", "bold", "black"}
        if v.lower() not in valid_weights:
            raise ValueError(f"Invalid font weight: {v}. Must be one of {valid_weights}")
        return v.lower()

    @field_validator('horizontal_align')
    def validate_horizontal_align(cls, v):
        valid_aligns = {"left", "center", "right"}
        if v.lower() not in valid_aligns:
            raise ValueError(f"Invalid alignment: {v}. Must be one of {valid_aligns}")
        return v.lower()

    class Config:
        json_schema_extra = {
            "example": {
                "color": "#FFFFFF",
                "font_size_multiplier": 1.2,
                "font_weight": "bold",
                "shadow": {"enabled": True, "color": "#000000"},
                "outline": {"enabled": False},
                "horizontal_align": "center"
            }
        }


class TextCustomization(BaseModel):
    """Per-element text customization (Phase 1 feature)."""
    headline: Optional[TextElementStyle] = Field(default=None, description="Headline styling")
    subheadline: Optional[TextElementStyle] = Field(default=None, description="Subheadline styling")
    cta: Optional[TextElementStyle] = Field(default=None, description="CTA styling")

    class Config:
        json_schema_extra = {
            "example": {
                "headline": {
                    "color": "#FFFFFF",
                    "font_weight": "bold",
                    "shadow": {"enabled": True}
                },
                "cta": {
                    "color": "#FF6600",
                    "outline": {"enabled": True, "color": "#FFFFFF", "width": 2}
                }
            }
        }


class PostProcessingConfig(BaseModel):
    """Post-processing configuration (Phase 1 feature)."""
    enabled: bool = Field(default=False, description="Enable post-processing")
    sharpening: bool = Field(default=True, description="Apply sharpening")
    sharpening_radius: float = Field(default=2.0, ge=0.1, le=10.0, description="Sharpening radius")
    sharpening_amount: int = Field(default=150, ge=0, le=300, description="Sharpening amount (percentage)")
    color_correction: bool = Field(default=True, description="Apply color correction")
    contrast_boost: float = Field(default=1.1, ge=1.0, le=2.0, description="Contrast boost multiplier")
    saturation_boost: float = Field(default=1.05, ge=1.0, le=2.0, description="Saturation boost multiplier")

    class Config:
        json_schema_extra = {
            "example": {
                "enabled": True,
                "sharpening": True,
                "sharpening_radius": 2.0,
                "sharpening_amount": 150,
                "color_correction": True,
                "contrast_boost": 1.15,
                "saturation_boost": 1.10
            }
        }


class ComprehensiveBrandGuidelines(BaseModel):
    """Brand guidelines extracted from external documents."""
    source_file: str = Field(..., description="Source guideline document path")
    primary_colors: List[str] = Field(default_factory=list, description="Primary brand colors (hex)")
    secondary_colors: Optional[List[str]] = Field(default_factory=list, description="Secondary colors")
    primary_font: str = Field(default="Arial", description="Primary font family")
    secondary_font: Optional[str] = Field(default=None, description="Secondary font family")
    brand_voice: str = Field(default="Professional", description="Brand voice and tone")
    photography_style: str = Field(default="Modern", description="Photography style guidelines")
    prohibited_uses: List[str] = Field(default_factory=list, description="Prohibited brand uses")
    prohibited_elements: List[str] = Field(default_factory=list, description="Prohibited visual elements")
    approved_taglines: List[str] = Field(default_factory=list, description="Approved brand taglines")

    # Logo placement and sizing
    logo_placement: str = Field(default="bottom-right", description="Logo position: top-left, top-right, bottom-left, bottom-right")
    logo_clearspace: int = Field(default=20, description="Minimum logo clearspace in pixels from edges")
    logo_min_size: int = Field(default=50, description="Minimum logo width in pixels")
    logo_max_size: int = Field(default=200, description="Maximum logo width in pixels")
    logo_opacity: float = Field(default=1.0, ge=0.0, le=1.0, description="Logo opacity (0.0-1.0, 1.0=fully opaque)")
    logo_scale: float = Field(default=0.15, ge=0.05, le=0.5, description="Logo size as percentage of image width (0.05-0.5)")

    # Text overlay customization (LEGACY - for backward compatibility)
    text_shadow: bool = Field(default=True, description="Enable drop shadow on text overlays")
    text_color: str = Field(default="#FFFFFF", description="Text overlay color (hex)")
    text_shadow_color: str = Field(default="#000000", description="Text shadow color (hex)")
    text_background: bool = Field(default=False, description="Enable semi-transparent background box behind text")
    text_background_color: str = Field(default="#000000", description="Text background box color (hex)")
    text_background_opacity: float = Field(default=0.5, ge=0.0, le=1.0, description="Text background opacity (0.0-1.0)")

    # NEW: Per-element text customization (Phase 1) - takes precedence over legacy settings
    text_customization: Optional[TextCustomization] = Field(default=None, description="Per-element text styling")

    # NEW: Post-processing configuration (Phase 1)
    post_processing: Optional[PostProcessingConfig] = Field(default=None, description="Image post-processing settings")

    class Config:
        json_schema_extra = {
            "example": {
                "source_file": "brand_guidelines.pdf",
                "primary_colors": ["#0066FF", "#1A1A1A"],
                "primary_font": "Montserrat",
                "brand_voice": "Bold, innovative, customer-focused",
                "photography_style": "Clean, modern, minimalist product photography"
            }
        }


class LegalComplianceGuidelines(BaseModel):
    """Legal compliance guidelines for content validation."""
    source_file: str = Field(..., description="Source guideline document path")

    # Prohibited content
    prohibited_words: List[str] = Field(
        default_factory=list,
        description="Words that must not appear in any content"
    )
    prohibited_phrases: List[str] = Field(
        default_factory=list,
        description="Phrases that must not appear in any content"
    )

    # Required disclaimers
    required_disclaimers: Dict[str, str] = Field(
        default_factory=dict,
        description="Required disclaimer text by category (e.g., 'financial', 'health')"
    )

    # Claims and restrictions
    prohibited_claims: List[str] = Field(
        default_factory=list,
        description="Marketing claims that cannot be made (e.g., 'cure cancer', 'guaranteed results')"
    )
    restricted_terms: Dict[str, List[str]] = Field(
        default_factory=dict,
        description="Terms that require specific context or disclaimers"
    )

    # Age and audience restrictions
    age_restrictions: Optional[int] = Field(
        default=None,
        description="Minimum age requirement (e.g., 18 for alcohol)"
    )
    restricted_audiences: List[str] = Field(
        default_factory=list,
        description="Audiences that cannot be targeted (e.g., 'children', 'minors')"
    )

    # Geographic restrictions
    restricted_regions: List[str] = Field(
        default_factory=list,
        description="Regions/countries where content is prohibited"
    )

    # Industry-specific compliance
    industry_regulations: List[str] = Field(
        default_factory=list,
        description="Applicable regulations (e.g., 'FDA', 'FTC', 'GDPR', 'COPPA')"
    )

    # Trademark and copyright
    protected_trademarks: List[str] = Field(
        default_factory=list,
        description="Competitor trademarks that must not be used"
    )

    # Content standards
    require_substantiation: bool = Field(
        default=False,
        description="Whether claims require scientific substantiation"
    )
    prohibit_superlatives: bool = Field(
        default=False,
        description="Whether superlatives like 'best', 'perfect' are prohibited"
    )

    # Locale-specific restrictions
    locale_restrictions: Dict[str, Dict[str, Any]] = Field(
        default_factory=dict,
        description="Locale-specific legal restrictions"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "source_file": "legal_guidelines.yaml",
                "prohibited_words": ["guarantee", "free", "cure"],
                "prohibited_claims": ["guaranteed results", "clinically proven"],
                "age_restrictions": 18,
                "industry_regulations": ["FTC", "FDA"]
            }
        }


class LocalizationGuidelines(BaseModel):
    """Localization guidelines for multi-market campaigns."""
    source_file: str = Field(..., description="Source guideline document path")
    supported_locales: List[str] = Field(default_factory=list, description="List of supported locales")
    market_specific_rules: Dict[str, Dict[str, Any]] = Field(
        default_factory=dict,
        description="Market-specific rules and preferences"
    )
    prohibited_terms: Dict[str, List[str]] = Field(
        default_factory=dict,
        description="Prohibited terms per locale"
    )
    translation_glossary: Dict[str, Dict[str, str]] = Field(
        default_factory=dict,
        description="Translation glossary per locale"
    )
    tone_guidelines: Optional[Dict[str, str]] = Field(
        default_factory=dict,
        description="Tone guidelines per locale"
    )
    cultural_considerations: Optional[Dict[str, List[str]]] = Field(
        default_factory=dict,
        description="Cultural considerations per locale"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "source_file": "localization_rules.yaml",
                "supported_locales": ["en-US", "es-MX", "fr-CA"],
                "market_specific_rules": {
                    "es-MX": {"tone": "warm", "formality": "formal"}
                },
                "prohibited_terms": {
                    "es-MX": ["barato", "oferta"]
                }
            }
        }


class CampaignBrief(BaseModel):
    """Complete campaign brief with all configuration."""
    campaign_id: str = Field(..., description="Unique campaign identifier")
    campaign_name: str = Field(..., description="Campaign display name")
    brand_name: str = Field(..., description="Brand name")
    target_market: Optional[str] = Field(default="Global", description="Target market")
    target_audience: Optional[str] = Field(default="General", description="Target audience")
    campaign_message: CampaignMessage = Field(..., description="Default campaign message")
    products: List[Product] = Field(..., min_length=1, description="List of products")
    aspect_ratios: List[str] = Field(
        default=["1:1", "9:16", "16:9"],
        description="Target aspect ratios"
    )
    output_formats: List[str] = Field(
        default=["png", "jpg"],
        description="Output image formats"
    )
    image_generation_backend: str = Field(
        default="firefly",
        description="Image generation backend: 'firefly', 'openai', 'gemini', or 'claude'"
    )
    brand_guidelines_file: Optional[str] = Field(
        default=None,
        description="Path to brand guidelines document"
    )
    localization_guidelines_file: Optional[str] = Field(
        default=None,
        description="Path to localization guidelines document"
    )
    legal_compliance_file: Optional[str] = Field(
        default=None,
        description="Path to legal compliance guidelines document"
    )
    enable_localization: bool = Field(
        default=False,
        description="Enable multi-locale generation"
    )
    target_locales: List[str] = Field(
        default_factory=lambda: ["en-US"],
        description="Target locales for campaign"
    )

    @field_validator('products')
    def validate_products(cls, v):
        if len(v) < 1:
            raise ValueError("At least one product is required")
        return v

    @field_validator('aspect_ratios')
    def validate_aspect_ratios(cls, v):
        valid_ratios = {"1:1", "9:16", "16:9", "4:5"}
        for ratio in v:
            if ratio not in valid_ratios:
                raise ValueError(f"Invalid aspect ratio: {ratio}. Must be one of {valid_ratios}")
        return v

    @field_validator('image_generation_backend')
    def validate_backend(cls, v):
        valid_backends = {"firefly", "openai", "dall-e", "dalle", "gemini", "imagen", "claude"}
        if v.lower() not in valid_backends:
            raise ValueError(
                f"Invalid image generation backend: {v}. "
                f"Must be one of {valid_backends}"
            )
        return v.lower()

    class Config:
        json_schema_extra = {
            "example": {
                "campaign_id": "SUMMER2026",
                "campaign_name": "Summer Collection Launch",
                "brand_name": "TechStyle",
                "campaign_message": {
                    "locale": "en-US",
                    "headline": "Summer Innovation",
                    "subheadline": "Discover the Future",
                    "cta": "Explore Now"
                },
                "products": [],
                "enable_localization": True,
                "target_locales": ["en-US", "es-MX", "fr-CA"]
            }
        }


class GeneratedAsset(BaseModel):
    """Metadata for a generated campaign asset."""
    product_id: str = Field(..., description="Associated product ID")
    locale: str = Field(..., description="Asset locale")
    aspect_ratio: str = Field(..., description="Asset aspect ratio")
    file_path: str = Field(..., description="Path to generated asset file")
    generation_method: str = Field(..., description="Generation method (firefly, reuse, etc.)")
    timestamp: datetime = Field(default_factory=datetime.now, description="Generation timestamp")
    metadata: Optional[Dict[str, Any]] = Field(
        default_factory=dict,
        description="Additional metadata"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "product_id": "PROD-001",
                "locale": "en-US",
                "aspect_ratio": "1:1",
                "file_path": "/output/campaign/en-US/PROD-001/1x1/asset.png",
                "generation_method": "firefly",
                "timestamp": "2026-01-13T10:30:00"
            }
        }


class TechnicalMetrics(BaseModel):
    """Advanced technical metrics for campaign generation."""
    backend_used: str = Field(..., description="AI backend used (firefly, openai, gemini)")
    total_api_calls: int = Field(default=0, description="Total API calls made")
    cache_hits: int = Field(default=0, description="Number of cache hits (hero image reuse)")
    cache_misses: int = Field(default=0, description="Number of cache misses")
    cache_hit_rate: float = Field(default=0.0, description="Cache hit rate percentage (0-100)")
    retry_count: int = Field(default=0, description="Total number of retries across all operations")
    retry_reasons: List[str] = Field(default_factory=list, description="Reasons for retries")
    avg_api_response_time_ms: float = Field(default=0.0, description="Average API response time in milliseconds")
    min_api_response_time_ms: float = Field(default=0.0, description="Minimum API response time")
    max_api_response_time_ms: float = Field(default=0.0, description="Maximum API response time")
    image_processing_time_ms: float = Field(default=0.0, description="Total image processing time")
    localization_time_ms: float = Field(default=0.0, description="Total localization time")
    compliance_check_time_ms: float = Field(default=0.0, description="Total compliance checking time")
    peak_memory_mb: float = Field(default=0.0, description="Peak memory usage in MB")
    system_info: Dict[str, str] = Field(default_factory=dict, description="System environment details")
    full_error_traces: List[Dict[str, str]] = Field(default_factory=list, description="Full error stack traces")


class BusinessMetrics(BaseModel):
    """Business-relevant metrics for ROI and efficiency analysis."""
    time_saved_vs_manual_hours: float = Field(
        default=0.0,
        description="Time saved vs manual process (assuming 3-5 days = 72-120 hours)"
    )
    time_saved_percentage: float = Field(
        default=0.0,
        description="Percentage time saved vs manual (0-100)"
    )
    cost_savings_percentage: float = Field(
        default=0.0,
        description="Estimated cost savings percentage vs manual (70-90%)"
    )
    manual_baseline_cost: float = Field(
        default=2700.0,
        description="Estimated manual production cost baseline"
    )
    estimated_manual_cost: float = Field(
        default=0.0,
        description="What this campaign would cost manually"
    )
    estimated_savings: float = Field(
        default=0.0,
        description="Estimated dollar savings vs manual"
    )
    roi_multiplier: float = Field(
        default=0.0,
        description="ROI multiplier (savings / actual cost spent)"
    )
    labor_hours_saved: float = Field(
        default=0.0,
        description="Estimated labor hours saved (at $50/hr avg)"
    )
    compliance_pass_rate: float = Field(
        default=100.0,
        description="Percentage of content that passed compliance (0-100)"
    )
    asset_reuse_efficiency: float = Field(
        default=0.0,
        description="Percentage of API calls saved through hero image reuse (0-100)"
    )
    avg_time_per_locale_seconds: float = Field(
        default=0.0,
        description="Average processing time per locale"
    )
    avg_time_per_asset_seconds: float = Field(
        default=0.0,
        description="Average processing time per asset"
    )
    localization_efficiency_score: float = Field(
        default=0.0,
        description="Localization efficiency (assets per hour)"
    )


class CampaignOutput(BaseModel):
    """Complete campaign output with all generated assets and metadata."""
    campaign_id: str = Field(..., description="Campaign identifier")
    campaign_name: str = Field(..., description="Campaign name")
    generated_assets: List[GeneratedAsset] = Field(
        default_factory=list,
        description="List of all generated assets"
    )
    total_assets: int = Field(default=0, description="Total number of assets generated")
    locales_processed: List[str] = Field(default_factory=list, description="Locales processed")
    products_processed: List[str] = Field(default_factory=list, description="Products processed")
    processing_time_seconds: float = Field(default=0.0, description="Total processing time")
    success_rate: float = Field(default=1.0, description="Success rate (0-1)")
    errors: List[str] = Field(default_factory=list, description="Any errors encountered")
    generation_timestamp: datetime = Field(
        default_factory=datetime.now,
        description="Generation completion timestamp"
    )

    # Enhanced metrics (v1.3.0+)
    technical_metrics: Optional[TechnicalMetrics] = Field(
        default=None,
        description="Advanced technical metrics"
    )
    business_metrics: Optional[BusinessMetrics] = Field(
        default=None,
        description="Business-relevant metrics for ROI analysis"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "campaign_id": "SUMMER2026",
                "campaign_name": "Summer Collection",
                "generated_assets": [],
                "total_assets": 12,
                "locales_processed": ["en-US", "es-MX"],
                "products_processed": ["PROD-001", "PROD-002"],
                "processing_time_seconds": 145.3,
                "success_rate": 0.95,
                "technical_metrics": {
                    "backend_used": "firefly",
                    "total_api_calls": 15,
                    "cache_hits": 10,
                    "cache_hit_rate": 66.7
                },
                "business_metrics": {
                    "time_saved_vs_manual_hours": 95.9,
                    "cost_savings_percentage": 89.0,
                    "roi_multiplier": 8.5
                }
            }
        }
