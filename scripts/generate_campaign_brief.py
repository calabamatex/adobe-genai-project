#!/usr/bin/env python3
"""
Campaign Brief Generator with Enhanced Prompt Strategies
Generates campaign brief JSON files implementing advanced prompt engineering.
"""

import json
import argparse
from typing import Dict, List, Optional
from datetime import datetime


# Prompt Templates by Category (from IMAGE_QUALITY_OPTIMIZATION.md)
PROMPT_TEMPLATES = {
    "electronics": {
        "style": "commercial product photography, professional studio shot, high-end tech aesthetic",
        "composition": "centered product placement, 3/4 angle view, negative space for text",
        "lighting": "three-point studio lighting, rim light highlighting edges, soft key light from 45 degrees",
        "background": "clean gradient background, subtle reflective surface, modern tech environment",
        "details": "focus on premium materials, visible texture detail, sharp product edges, crisp reflections",
        "negative": "cluttered, busy background, harsh shadows, overexposed highlights, blurry details"
    },
    "fashion": {
        "style": "high fashion editorial, lifestyle photography, contemporary aesthetic",
        "composition": "dynamic model pose, rule of thirds placement, lifestyle context",
        "lighting": "natural window lighting, soft diffused light, golden hour warmth",
        "background": "urban setting, minimalist interior, neutral tones",
        "details": "fabric texture visible, color accuracy critical, natural skin tones, movement captured",
        "negative": "stiff pose, artificial colors, harsh lighting, cluttered background"
    },
    "food": {
        "style": "food editorial photography, gourmet presentation, appetizing aesthetic",
        "composition": "overhead flat lay, 45-degree hero angle, styled with props",
        "lighting": "natural diffused lighting, soft shadows, warm color temperature",
        "background": "rustic wooden table, clean marble surface, textured fabric backdrop",
        "details": "steam visible, fresh ingredients, glistening surfaces, vibrant colors, sharp focus on food",
        "negative": "dull colors, messy presentation, harsh shadows, unappetizing, overprocessed"
    },
    "beauty": {
        "style": "beauty editorial, cosmetic product photography, luxury aesthetic",
        "composition": "centered product with lifestyle context, elegant arrangement, luxury props",
        "lighting": "soft beauty lighting, highlight shimmer and texture, no harsh shadows",
        "background": "minimal elegant backdrop, marble or silk textures, pastel colors",
        "details": "product label clearly visible, texture of formulation shown, premium packaging details",
        "negative": "cheap appearance, harsh lighting, cluttered, low quality rendering"
    },
    "automotive": {
        "style": "automotive photography, professional car advertisement, dynamic aesthetic",
        "composition": "3/4 front angle, dramatic low angle, environmental context",
        "lighting": "dramatic side lighting, studio or golden hour, highlighting curves and lines",
        "background": "open road, modern architecture, studio with dramatic backdrop",
        "details": "chrome reflections, paint finish quality, wheel detail, sharp body lines",
        "negative": "flat lighting, boring angle, cluttered background, poor reflections"
    },
    "premium_audio": {
        "style": "premium tech product photography, high-end audio aesthetic, luxury lifestyle",
        "composition": "centered with lifestyle context, detailed close-up shots, negative space for branding",
        "lighting": "dramatic studio lighting with rim lights, metallic highlights, soft key light",
        "background": "minimalist modern setting, dark gradient, subtle texture",
        "details": "material quality visible (metal, leather), controls clearly shown, premium craftsmanship details",
        "negative": "cheap plastic appearance, flat lighting, cluttered, low resolution"
    },
    "display_tech": {
        "style": "professional tech photography, modern display technology, sleek aesthetic",
        "composition": "angled to show screen content and design, environmental context showing use case",
        "lighting": "soft studio lighting, screen content backlit, minimal reflections on screen",
        "background": "modern workspace, minimalist desk setup, neutral professional environment",
        "details": "screen content sharp and vivid, bezel detail visible, premium materials shown, ports/connectors clear",
        "negative": "screen glare, blurry display content, cheap appearance, cluttered desk"
    }
}


def create_enhanced_prompt(
    base_description: str,
    category: str,
    custom_style: Optional[str] = None,
    custom_composition: Optional[str] = None,
    custom_lighting: Optional[str] = None,
    custom_background: Optional[str] = None,
    custom_details: Optional[str] = None
) -> str:
    """
    Create enhanced structured prompt from base description and template.

    Args:
        base_description: Basic product description
        category: Product category (electronics, fashion, food, etc.)
        custom_*: Optional custom overrides for each component

    Returns:
        Enhanced prompt string with all components
    """
    template = PROMPT_TEMPLATES.get(category, PROMPT_TEMPLATES["electronics"])

    # Use custom values if provided, otherwise use template
    style = custom_style or template["style"]
    composition = custom_composition or template["composition"]
    lighting = custom_lighting or template["lighting"]
    background = custom_background or template["background"]
    details = custom_details or template["details"]
    negative = template["negative"]

    # Build comprehensive prompt
    enhanced_prompt = (
        f"{base_description}, "
        f"{style}, "
        f"{composition}, "
        f"{lighting}, "
        f"{background}, "
        f"{details}"
    )

    return enhanced_prompt, negative


def generate_premium_audio_campaign() -> Dict:
    """Generate premium audio campaign brief (earbuds + headphones)."""

    # Product 1: Premium Wireless Earbuds
    earbuds_prompt, earbuds_negative = create_enhanced_prompt(
        base_description="premium true wireless earbuds in sleek charging case",
        category="premium_audio"
    )

    # Product 2: Premium Over-Ear Headphones
    headphones_prompt, headphones_negative = create_enhanced_prompt(
        base_description="premium over-ear wireless headphones with active noise cancellation",
        category="premium_audio",
        custom_details="leather ear cushions visible, metal headband detail, premium build quality, control buttons clearly shown"
    )

    campaign = {
        "campaign_id": "PREMIUM_AUDIO_2026",
        "campaign_name": "Premium Audio Experience 2026",
        "brand_name": "AudioElite Pro",
        "target_market": "Global",
        "target_audience": "Audiophiles and professionals aged 25-50 seeking premium audio quality",
        "campaign_message": {
            "locale": "en-US",
            "headline": "Experience Sound Perfection",
            "subheadline": "Premium Audio Engineering for Discerning Listeners",
            "cta": "Discover Premium Audio"
        },
        "products": [
            {
                "product_id": "EARBUDS-PRO-001",
                "product_name": "Elite True Wireless Earbuds Pro",
                "product_description": "Premium true wireless earbuds with adaptive ANC, spatial audio, and audiophile-grade sound drivers. 8-hour battery life with wireless charging case.",
                "product_category": "Premium Audio",
                "key_features": [
                    "Adaptive Active Noise Cancellation",
                    "Spatial Audio with head tracking",
                    "8 hours battery per charge (32 hours total)",
                    "Audiophile-grade sound drivers",
                    "Water resistant IPX5",
                    "Premium metal charging case"
                ],
                "generation_prompt": earbuds_prompt,
                "enhanced_generation": {
                    "base_prompt": "premium true wireless earbuds in sleek charging case",
                    "style_parameters": {
                        "photography_style": "commercial product photography",
                        "artistic_style": "high-end tech aesthetic",
                        "color_palette": ["metallic silver", "deep black", "subtle blue accent"],
                        "mood": "premium luxury",
                        "quality_level": "ultra high resolution 8K"
                    },
                    "composition": {
                        "primary_subject": "earbuds displayed in open charging case",
                        "viewing_angle": "3/4 angle from above",
                        "depth_of_field": "shallow DOF with sharp focus on earbuds",
                        "rule_of_thirds": True,
                        "negative_space": "ample space on right side for text overlay"
                    },
                    "lighting": {
                        "primary_light": "soft key light from 45 degrees",
                        "fill_light": "subtle fill to lift shadows",
                        "rim_light": "strong rim light highlighting metallic edges",
                        "color_temperature": "cool daylight 5500K",
                        "quality": "soft studio lighting"
                    },
                    "background": {
                        "type": "gradient",
                        "colors": ["deep charcoal", "midnight blue"],
                        "texture": "subtle reflective surface",
                        "style": "minimalist tech environment"
                    },
                    "details": {
                        "focus_areas": ["premium metal finish", "charging contacts", "brand logo"],
                        "texture_emphasis": "brushed metal texture on case",
                        "quality_indicators": "sharp edges, crisp reflections, visible craftsmanship"
                    },
                    "negative_prompt": earbuds_negative
                },
                "existing_assets": {}
            },
            {
                "product_id": "HEADPHONES-PRO-001",
                "product_name": "Elite Over-Ear Headphones Pro",
                "product_description": "Premium wireless over-ear headphones with advanced ANC, LDAC high-res audio, and 40-hour battery life. Luxurious leather ear cushions and aluminum construction.",
                "product_category": "Premium Audio",
                "key_features": [
                    "Advanced Hybrid ANC",
                    "LDAC high-resolution audio codec",
                    "40-hour battery life",
                    "Premium leather ear cushions",
                    "Aluminum and steel construction",
                    "Multi-point connectivity"
                ],
                "generation_prompt": headphones_prompt,
                "enhanced_generation": {
                    "base_prompt": "premium over-ear wireless headphones with active noise cancellation",
                    "style_parameters": {
                        "photography_style": "commercial product photography",
                        "artistic_style": "luxury audio equipment aesthetic",
                        "color_palette": ["matte black", "brushed aluminum", "rich brown leather"],
                        "mood": "professional premium",
                        "quality_level": "ultra high resolution 8K"
                    },
                    "composition": {
                        "primary_subject": "headphones positioned at elegant angle",
                        "viewing_angle": "3/4 side view showing ear cups and headband",
                        "depth_of_field": "medium DOF with primary focus on ear cup details",
                        "rule_of_thirds": True,
                        "negative_space": "clean space above for headline text"
                    },
                    "lighting": {
                        "primary_light": "dramatic side key light",
                        "fill_light": "soft fill maintaining detail in shadows",
                        "rim_light": "accent rim light on metal headband",
                        "color_temperature": "neutral 5000K",
                        "quality": "professional studio lighting setup"
                    },
                    "background": {
                        "type": "gradient",
                        "colors": ["charcoal gray", "warm black"],
                        "texture": "subtle fabric texture",
                        "style": "minimalist luxury studio"
                    },
                    "details": {
                        "focus_areas": ["leather ear cushion texture", "metal headband finish", "control buttons", "brand emblem"],
                        "texture_emphasis": "visible leather grain, brushed metal finish",
                        "quality_indicators": "premium build quality, precise manufacturing details, professional craftsmanship"
                    },
                    "negative_prompt": headphones_negative
                },
                "existing_assets": {}
            }
        ],
        "aspect_ratios": ["1:1", "9:16", "16:9"],
        "output_formats": ["png"],
        "image_generation_backend": "firefly",
        "brand_guidelines_file": "examples/guidelines/brand_guidelines.md",
        "localization_guidelines_file": "examples/guidelines/localization_rules.yaml",
        "enable_localization": True,
        "target_locales": ["en-US", "es-MX", "fr-FR", "de-DE", "ja-JP", "ko-KR"]
    }

    return campaign


def generate_premium_tech_campaign() -> Dict:
    """Generate premium tech campaign brief (earbuds + portable monitor)."""

    # Product 1: Premium Wireless Earbuds
    earbuds_prompt, earbuds_negative = create_enhanced_prompt(
        base_description="premium true wireless earbuds in charging case with metallic finish",
        category="premium_audio"
    )

    # Product 2: Portable 4K Monitor
    monitor_prompt, monitor_negative = create_enhanced_prompt(
        base_description="ultra-slim 15.6-inch 4K OLED portable monitor displaying vivid content",
        category="display_tech"
    )

    campaign = {
        "campaign_id": "PREMIUM_TECH_2026",
        "campaign_name": "Premium Tech Experience 2026",
        "brand_name": "TechStyle Elite",
        "target_market": "Global",
        "target_audience": "Tech professionals and content creators aged 30-50 seeking premium quality",
        "campaign_message": {
            "locale": "en-US",
            "headline": "Excellence in Every Detail",
            "subheadline": "Premium Technology for Professionals",
            "cta": "Explore Premium Tech"
        },
        "products": [
            {
                "product_id": "EARBUDS-ELITE-001",
                "product_name": "Elite Wireless Earbuds Pro Max",
                "product_description": "Premium true wireless earbuds with adaptive noise cancellation, spatial audio, and 8-hour battery life per charge. Crystal-clear highs and deep, powerful bass in an ultra-compact design.",
                "product_category": "Premium Audio",
                "key_features": [
                    "Adaptive Noise Cancellation",
                    "Spatial Audio with head tracking",
                    "8 hours battery (32 hours with case)",
                    "Premium sound drivers",
                    "Water and sweat resistant IPX4",
                    "Touch controls"
                ],
                "generation_prompt": earbuds_prompt,
                "enhanced_generation": {
                    "base_prompt": "premium true wireless earbuds in charging case with metallic finish",
                    "style_parameters": {
                        "photography_style": "commercial product photography",
                        "artistic_style": "luxury tech aesthetic",
                        "color_palette": ["titanium gray", "pearl white", "obsidian black"],
                        "mood": "professional luxury",
                        "quality_level": "8K ultra high resolution"
                    },
                    "composition": {
                        "primary_subject": "earbuds in open charging case",
                        "viewing_angle": "3/4 top-down angle",
                        "depth_of_field": "shallow with sharp focus on product",
                        "rule_of_thirds": True,
                        "negative_space": "clean space for brand messaging"
                    },
                    "lighting": {
                        "primary_light": "soft key light at 45 degrees",
                        "fill_light": "gentle fill to preserve detail",
                        "rim_light": "accent light highlighting metallic edges and curves",
                        "color_temperature": "daylight 5500K",
                        "quality": "professional studio three-point setup"
                    },
                    "background": {
                        "type": "gradient",
                        "colors": ["deep black", "charcoal"],
                        "texture": "glossy reflective surface with subtle texture",
                        "style": "high-end tech studio environment"
                    },
                    "details": {
                        "focus_areas": ["metallic case finish", "earbud design", "LED indicators"],
                        "texture_emphasis": "premium metal texture, smooth curves",
                        "quality_indicators": "sharp crisp edges, visible premium materials, precise manufacturing"
                    },
                    "negative_prompt": earbuds_negative
                },
                "existing_assets": {}
            },
            {
                "product_id": "MONITOR-ULTRA-001",
                "product_name": "UltraView Portable 4K OLED Monitor Pro",
                "product_description": "Professional-grade 15.6-inch 4K OLED portable monitor with USB-C connectivity, HDR10+ support, and ultra-slim 5mm design. Perfect for professionals on the go.",
                "product_category": "Display Technology",
                "key_features": [
                    "15.6-inch 4K OLED display",
                    "HDR10+ support with 100% DCI-P3",
                    "USB-C single cable power and video",
                    "Ultra-slim 5mm design",
                    "Auto-rotation and touch support",
                    "Built-in dual speakers"
                ],
                "generation_prompt": monitor_prompt,
                "enhanced_generation": {
                    "base_prompt": "ultra-slim 15.6-inch 4K OLED portable monitor displaying vivid content",
                    "style_parameters": {
                        "photography_style": "professional tech photography",
                        "artistic_style": "modern display technology aesthetic",
                        "color_palette": ["space gray aluminum", "deep blacks", "vivid screen colors"],
                        "mood": "professional premium",
                        "quality_level": "8K ultra high resolution"
                    },
                    "composition": {
                        "primary_subject": "portable monitor at elegant angle showing screen and design",
                        "viewing_angle": "3/4 angle showing screen content and slim profile",
                        "depth_of_field": "medium DOF with screen and body in focus",
                        "rule_of_thirds": True,
                        "negative_space": "space above and beside for text elements"
                    },
                    "lighting": {
                        "primary_light": "soft diffused key light",
                        "fill_light": "ambient fill maintaining detail",
                        "rim_light": "subtle rim light on edges",
                        "color_temperature": "neutral 5000K ambient",
                        "quality": "professional studio lighting with screen backlit"
                    },
                    "background": {
                        "type": "environment",
                        "colors": ["modern workspace", "minimalist desk", "neutral grays"],
                        "texture": "clean contemporary office setting",
                        "style": "professional workspace environment"
                    },
                    "details": {
                        "focus_areas": ["vivid screen display", "ultra-thin bezel", "aluminum body", "USB-C port"],
                        "texture_emphasis": "premium aluminum finish, OLED screen quality",
                        "quality_indicators": "sharp screen content, visible premium materials, precise engineering, professional color accuracy"
                    },
                    "negative_prompt": monitor_negative
                },
                "existing_assets": {}
            }
        ],
        "aspect_ratios": ["1:1", "9:16", "16:9"],
        "output_formats": ["png"],
        "image_generation_backend": "firefly",
        "brand_guidelines_file": "examples/guidelines/brand_guidelines.md",
        "localization_guidelines_file": "examples/guidelines/localization_rules.yaml",
        "enable_localization": True,
        "target_locales": ["en-US", "es-MX", "fr-FR", "de-DE", "ja-JP"]
    }

    return campaign


def generate_fashion_campaign() -> Dict:
    """Generate fashion/lifestyle campaign brief."""

    prompt, negative = create_enhanced_prompt(
        base_description="premium designer sneakers on lifestyle model",
        category="fashion"
    )

    campaign = {
        "campaign_id": "FASHION_SUMMER_2026",
        "campaign_name": "Summer Fashion Collection 2026",
        "brand_name": "StyleHouse",
        "target_market": "North America & Europe",
        "target_audience": "Fashion-conscious individuals aged 20-35",
        "campaign_message": {
            "locale": "en-US",
            "headline": "Define Your Style",
            "subheadline": "Premium Fashion for Modern Living",
            "cta": "Shop Collection"
        },
        "products": [
            {
                "product_id": "SNEAKERS-001",
                "product_name": "Premium Designer Sneakers",
                "product_description": "High-end designer sneakers with sustainable materials, contemporary design, and superior comfort.",
                "product_category": "Fashion Footwear",
                "key_features": [
                    "Sustainable materials",
                    "Contemporary design",
                    "Superior comfort cushioning",
                    "Premium leather and mesh"
                ],
                "generation_prompt": prompt,
                "enhanced_generation": {
                    "base_prompt": "premium designer sneakers on lifestyle model",
                    "style_parameters": {
                        "photography_style": "high fashion editorial",
                        "artistic_style": "contemporary lifestyle aesthetic",
                        "color_palette": ["neutral earth tones", "cream", "sage green"],
                        "mood": "aspirational lifestyle",
                        "quality_level": "high resolution editorial quality"
                    },
                    "composition": {
                        "primary_subject": "sneakers on model in lifestyle context",
                        "viewing_angle": "eye level candid shot",
                        "depth_of_field": "medium DOF with sneakers in focus",
                        "rule_of_thirds": True,
                        "negative_space": "natural environmental negative space"
                    },
                    "lighting": {
                        "primary_light": "natural window light",
                        "fill_light": "soft ambient indoor light",
                        "rim_light": "subtle outdoor backlight",
                        "color_temperature": "warm 4500K golden hour",
                        "quality": "soft natural lighting"
                    },
                    "background": {
                        "type": "environment",
                        "colors": ["urban setting", "minimalist interior", "neutral tones"],
                        "texture": "natural textures, concrete, wood",
                        "style": "contemporary lifestyle environment"
                    },
                    "details": {
                        "focus_areas": ["sneaker design details", "material texture", "laces", "sole"],
                        "texture_emphasis": "leather texture, mesh detail, stitching",
                        "quality_indicators": "natural lifestyle context, authentic moment, premium product detail"
                    },
                    "negative_prompt": negative
                },
                "existing_assets": {}
            }
        ],
        "aspect_ratios": ["1:1", "9:16", "16:9", "4:5"],
        "output_formats": ["png"],
        "image_generation_backend": "dalle",
        "brand_guidelines_file": "examples/guidelines/brand_guidelines.md",
        "localization_guidelines_file": "examples/guidelines/localization_rules.yaml",
        "enable_localization": True,
        "target_locales": ["en-US", "fr-FR", "de-DE"]
    }

    return campaign


def main():
    """Main entry point for campaign brief generator."""
    parser = argparse.ArgumentParser(
        description="Generate campaign brief JSON files with enhanced prompt strategies",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate premium audio campaign
  python generate_campaign_brief.py --template premium_audio --output premium_audio.json

  # Generate premium tech campaign
  python generate_campaign_brief.py --template premium_tech --output premium_tech.json

  # Generate fashion campaign
  python generate_campaign_brief.py --template fashion --output fashion.json

  # List available templates
  python generate_campaign_brief.py --list-templates
        """
    )

    parser.add_argument(
        "--template",
        type=str,
        choices=["premium_audio", "premium_tech", "fashion"],
        help="Campaign template to generate"
    )

    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output JSON file path (default: examples/{template}_campaign.json)"
    )

    parser.add_argument(
        "--list-templates",
        action="store_true",
        help="List available campaign templates and prompt categories"
    )

    parser.add_argument(
        "--pretty",
        action="store_true",
        default=True,
        help="Pretty print JSON output (default: True)"
    )

    args = parser.parse_args()

    if args.list_templates:
        print("\n📋 Available Campaign Templates:")
        print("  - premium_audio: Premium audio products (earbuds + headphones)")
        print("  - premium_tech: Premium tech products (earbuds + portable monitor)")
        print("  - fashion: Fashion/lifestyle products (sneakers)")
        print("\n🎨 Available Prompt Categories:")
        for category in PROMPT_TEMPLATES.keys():
            print(f"  - {category}")
        print()
        return

    if not args.template:
        parser.error("--template is required (or use --list-templates)")

    # Generate campaign based on template
    print(f"🎨 Generating {args.template} campaign brief...")

    if args.template == "premium_audio":
        campaign = generate_premium_audio_campaign()
    elif args.template == "premium_tech":
        campaign = generate_premium_tech_campaign()
    elif args.template == "fashion":
        campaign = generate_fashion_campaign()

    # Determine output path
    if args.output:
        output_path = args.output
    else:
        output_path = f"examples/{args.template}_campaign_enhanced.json"

    # Write campaign brief to file
    with open(output_path, 'w') as f:
        if args.pretty:
            json.dump(campaign, f, indent=2)
        else:
            json.dump(campaign, f)

    print(f"✅ Campaign brief generated: {output_path}")
    print(f"   Campaign ID: {campaign['campaign_id']}")
    print(f"   Products: {len(campaign['products'])}")
    print(f"   Locales: {len(campaign['target_locales'])}")
    print(f"   Backend: {campaign['image_generation_backend']}")

    # Display enhanced prompt structure
    print(f"\n📝 Enhanced Prompt Features:")
    for product in campaign['products']:
        if 'enhanced_generation' in product:
            print(f"   {product['product_name']}:")
            eg = product['enhanced_generation']
            if 'style_parameters' in eg:
                print(f"      ✓ Style parameters (photography, mood, quality)")
            if 'composition' in eg:
                print(f"      ✓ Composition rules (angle, DOF, negative space)")
            if 'lighting' in eg:
                print(f"      ✓ Lighting setup (3-point, color temp)")
            if 'background' in eg:
                print(f"      ✓ Background design")
            if 'details' in eg:
                print(f"      ✓ Detail focus areas")
            if 'negative_prompt' in eg:
                print(f"      ✓ Negative prompt")


if __name__ == "__main__":
    main()
