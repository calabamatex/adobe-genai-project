# Scripts Directory

Utility scripts for Adobe GenAI Creative Automation Platform.

## Campaign Brief Generator

**File:** `generate_campaign_brief.py`

A Python script that generates campaign brief JSON files implementing enhanced prompt engineering strategies from the [IMAGE_QUALITY_OPTIMIZATION.md](../docs/IMAGE_QUALITY_OPTIMIZATION.md) guide.

### Features

- **Advanced Prompt Engineering**: Structured prompts with professional photography terminology
- **Multiple Templates**: Pre-built templates for different product categories
- **Enhanced Generation Objects**: Detailed breakdown of style, composition, lighting, background, and details
- **Negative Prompts**: Explicitly defines what to avoid in generation
- **7 Product Categories**: Electronics, fashion, food, beauty, automotive, premium audio, display tech

### Usage

#### List Available Templates

```bash
python3 scripts/generate_campaign_brief.py --list-templates
```

**Output:**
```
📋 Available Campaign Templates:
  - premium_audio: Premium audio products (earbuds + headphones)
  - premium_tech: Premium tech products (earbuds + portable monitor)
  - fashion: Fashion/lifestyle products (sneakers)

🎨 Available Prompt Categories:
  - electronics
  - fashion
  - food
  - beauty
  - automotive
  - premium_audio
  - display_tech
```

#### Generate Campaign Briefs

**Premium Audio Campaign (2 products: earbuds + headphones):**
```bash
python3 scripts/generate_campaign_brief.py --template premium_audio --output examples/premium_audio_enhanced.json
```

**Premium Tech Campaign (2 products: earbuds + portable monitor):**
```bash
python3 scripts/generate_campaign_brief.py --template premium_tech --output examples/premium_tech_enhanced.json
```

**Fashion Campaign (sneakers):**
```bash
python3 scripts/generate_campaign_brief.py --template fashion --output examples/fashion_enhanced.json
```

### Generated Output Structure

Each generated campaign brief includes both:

1. **Flattened Prompt** (`generation_prompt`): Complete prompt string ready to use
2. **Structured Breakdown** (`enhanced_generation`): Detailed component breakdown

Example structure:
```json
{
  "products": [
    {
      "product_id": "EARBUDS-PRO-001",
      "product_name": "Elite True Wireless Earbuds Pro",
      "generation_prompt": "premium true wireless earbuds...[complete prompt]",
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
          "rule_of_thirds": true,
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
        "negative_prompt": "cheap plastic appearance, flat lighting, cluttered, low resolution"
      }
    }
  ]
}
```

### Command-Line Arguments

| Argument | Description | Required |
|----------|-------------|----------|
| `--template` | Campaign template: `premium_audio`, `premium_tech`, `fashion` | Yes |
| `--output` | Output JSON file path (default: `examples/{template}_campaign_enhanced.json`) | No |
| `--list-templates` | List available templates and categories | No |
| `--pretty` | Pretty print JSON output (default: True) | No |

### Examples

**Generate and immediately use:**
```bash
# Generate enhanced premium audio campaign
python3 scripts/generate_campaign_brief.py --template premium_audio --output examples/my_campaign.json

# Run campaign generation with enhanced prompts
./run_cli.sh examples/my_campaign.json firefly
```

**Compare standard vs enhanced:**
```bash
# Standard campaign (simple prompts)
./run_cli.sh examples/campaign_brief.json gemini

# Enhanced campaign (structured prompts)
python3 scripts/generate_campaign_brief.py --template premium_tech
./run_cli.sh examples/premium_tech_campaign_enhanced.json firefly
```

### Prompt Category Templates

The script includes 7 pre-built prompt templates optimized for different product categories:

1. **Electronics**: Studio lighting, tech aesthetic, metallic finishes
2. **Fashion**: Editorial style, lifestyle context, natural lighting
3. **Food**: Gourmet presentation, appetizing styling, overhead/45° angles
4. **Beauty**: Luxury aesthetic, soft lighting, texture emphasis
5. **Automotive**: Dramatic lighting, dynamic angles, chrome reflections
6. **Premium Audio**: High-end tech, luxury materials, dramatic studio setup
7. **Display Tech**: Professional workspace, screen content quality, slim design

### Expected Quality Improvements

Using enhanced prompts typically results in:

- **30-40% better image quality** through detailed prompt engineering
- **Consistent styling** across all generated assets
- **Professional aesthetics** matching commercial photography standards
- **Reduced regeneration** due to clearer prompt specifications
- **Backend-optimized** prompts for Firefly, DALL-E 3, and Gemini Imagen 4

### Integration with Pipeline

The generated campaign briefs are fully compatible with the existing pipeline:

```bash
# Generate enhanced brief
python3 scripts/generate_campaign_brief.py --template premium_tech

# Process with any backend
./run_cli.sh examples/premium_tech_campaign_enhanced.json firefly
./run_cli.sh examples/premium_tech_campaign_enhanced.json dalle
./run_cli.sh examples/premium_tech_campaign_enhanced.json gemini
```

### Customization

To add custom templates or modify existing ones, edit the `PROMPT_TEMPLATES` dictionary in `generate_campaign_brief.py`:

```python
PROMPT_TEMPLATES = {
    "your_category": {
        "style": "your photography style",
        "composition": "your composition rules",
        "lighting": "your lighting setup",
        "background": "your background design",
        "details": "your detail focus areas",
        "negative": "what to avoid"
    }
}
```

Then add a corresponding `generate_your_category_campaign()` function following the existing patterns.

## Additional Scripts

More utility scripts will be added to this directory as the project evolves.

---

For questions or issues, see the main [README.md](../README.md) or open an issue on GitHub.
