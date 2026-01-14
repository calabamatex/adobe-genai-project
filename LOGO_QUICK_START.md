# Logo Placement Quick Start

Add your brand logo to generated campaign images in 4 easy steps.

## Step 1: Prepare Your Logo

Place your logo file (PNG recommended) in the logos directory:

```bash
cp /path/to/your/logo.png examples/assets/logos/my-brand-logo.png
```

**Requirements:**
- Format: PNG with transparent background (best)
- Size: 500x500 pixels or larger
- File size: Under 1 MB

## Step 2: Create Brand Guidelines

Create or update your brand guidelines YAML file:

```yaml
# examples/guidelines/my_brand.yaml
source_file: "examples/guidelines/my_brand.yaml"

primary_colors:
  - "#0066FF"

primary_font: "Helvetica"
brand_voice: "Modern and innovative"
photography_style: "Clean product photography"

# Logo configuration
logo_placement: "bottom-right"      # Where to place logo
logo_clearspace: 30                 # Spacing from edges
logo_scale: 0.15                    # 15% of image width
logo_opacity: 1.0                   # Fully visible
```

## Step 3: Reference Logo in Campaign

Add the logo to your campaign brief JSON:

```json
{
  "campaign_id": "MY_CAMPAIGN",
  "campaign_name": "My Campaign",
  "brand_name": "My Brand",
  "campaign_message": {
    "locale": "en-US",
    "headline": "Great Products",
    "subheadline": "Amazing Quality",
    "cta": "Shop Now"
  },
  "products": [
    {
      "product_id": "PRODUCT-001",
      "product_name": "My Product",
      "product_description": "Great product",
      "product_category": "General",
      "key_features": ["Feature 1", "Feature 2"],
      "existing_assets": {
        "logo": "examples/assets/logos/my-brand-logo.png"
      },
      "generation_prompt": "modern product on white background"
    }
  ],
  "aspect_ratios": ["1:1", "9:16"],
  "output_formats": ["png"],
  "image_generation_backend": "openai",
  "brand_guidelines_file": "examples/guidelines/my_brand.yaml"
}
```

## Step 4: Generate Campaign

Run the campaign generator:

```bash
./run_cli.sh examples/my_campaign.json
```

Your generated images will have your logo automatically placed!

## Common Logo Styles

### Standard Logo (Bottom-Right)
```yaml
logo_placement: "bottom-right"
logo_scale: 0.15
logo_opacity: 1.0
logo_clearspace: 30
```

### Watermark (Top-Left, Semi-Transparent)
```yaml
logo_placement: "top-left"
logo_scale: 0.18
logo_opacity: 0.4        # 40% transparent
logo_clearspace: 25
```

### Prominent Branding (Top-Right, Large)
```yaml
logo_placement: "top-right"
logo_scale: 0.25         # 25% of image width
logo_opacity: 1.0
logo_clearspace: 40
```

## Logo Placement Options

```
┌─────────────────────────┐
│ TOP-LEFT    TOP-RIGHT   │
│                         │
│     Campaign Text       │
│     Appears Here        │
│                         │
│ BOTTOM-LEFT BOTTOM-RIGHT│ ← Default
└─────────────────────────┘
```

- **bottom-right**: Default, doesn't overlap text
- **top-left**: Watermark style
- **top-right**: Visible but clear of text
- **bottom-left**: Alternative corner

## Configuration Options

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `logo_placement` | top-left, top-right, bottom-left, bottom-right | bottom-right | Corner position |
| `logo_clearspace` | 10-100 pixels | 20 | Space from edges |
| `logo_min_size` | 20-200 pixels | 50 | Minimum width |
| `logo_max_size` | 100-500 pixels | 200 | Maximum width |
| `logo_scale` | 0.05-0.5 | 0.15 | % of image width |
| `logo_opacity` | 0.0-1.0 | 1.0 | Transparency |

## Troubleshooting

**Logo not appearing?**
- Check file path is correct
- Verify file exists: `ls examples/assets/logos/my-brand-logo.png`
- Ensure brand guidelines file is referenced in campaign

**Logo too small/large?**
- Adjust `logo_scale` (0.10 = smaller, 0.25 = larger)
- Adjust `logo_max_size` for upper limit

**Need watermark effect?**
- Set `logo_opacity: 0.3` (30% visible)
- Use `logo_placement: "top-left"`

## Next Steps

- **Full Documentation**: `docs/LOGO_PLACEMENT.md`
- **Logo Requirements**: `examples/assets/logos/README.md`
- **Example Configs**: `examples/guidelines/brand_with_logo.yaml`
- **Test Campaign**: `examples/logo_placement_test.json`

## Examples

Test the built-in examples:

```bash
# Standard logo placement
./run_cli.sh examples/logo_placement_test.json

# View example configurations
cat examples/guidelines/brand_with_logo.yaml
cat examples/guidelines/brand_logo_watermark.yaml
```
