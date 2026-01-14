# Brand Guidelines Configuration

This directory contains example brand guideline files that can be referenced in campaign briefs.

## Text Overlay Customization

You have full control over text appearance in generated images through brand guidelines.

### Available Text Customization Options

All text overlay settings are configured in your brand guidelines YAML file:

```yaml
# Text overlay customization (all fields are optional)
text_color: "#FFFFFF"              # Text color (hex) - default: white
text_shadow: true                  # Enable/disable drop shadows - default: true
text_shadow_color: "#000000"       # Shadow color (hex) - default: black
text_background: false             # Enable semi-transparent box - default: false
text_background_color: "#000000"   # Background box color (hex) - default: black
text_background_opacity: 0.5       # Background opacity (0.0-1.0) - default: 0.5
```

### Default Behavior (No Brand Guidelines)

Without brand guidelines specified:
- **Text color**: White (#FFFFFF)
- **Text shadows**: Enabled
- **Shadow color**: Black (#000000)
- **Shadow offset**: 1% of minimum image dimension
- **Background box**: Disabled

## Configuration Examples

### 1. Clean Design (No Shadows)

For minimalist, clean designs with bright backgrounds:

```yaml
# brand_no_shadow.yaml
text_color: "#FFFFFF"
text_shadow: false          # No shadows
text_background: false      # No background box
```

**Test:** `./run_cli.sh examples/no_shadow_test.json`

### 2. Custom Brand Colors

Use your brand colors for text overlays:

```yaml
# brand_custom_colors.yaml
primary_colors:
  - "#0066FF"  # Electric Blue

text_color: "#0066FF"        # Use brand blue for text
text_shadow: true            # Enable shadows for contrast
text_shadow_color: "#FFFFFF" # White shadow on dark backgrounds
text_background: false
```

**Test:** `./run_cli.sh examples/text_customization_test.json`

### 3. Semi-Transparent Background Box

Modern style with background overlay for maximum readability:

```yaml
# brand_with_background.yaml
text_color: "#FFFFFF"              # White text
text_shadow: false                 # No shadow needed
text_background: true              # Enable background box
text_background_color: "#1A1A1A"   # Dark background
text_background_opacity: 0.7       # 70% opacity
```

**Test:** `./run_cli.sh examples/text_background_test.json`

### 4. High Contrast (Default)

Standard high-contrast design for maximum visibility:

```yaml
# default_style.yaml
text_color: "#FFFFFF"        # White text
text_shadow: true            # Black shadow
text_shadow_color: "#000000"
text_background: false
```

## Using Brand Guidelines in Campaigns

Reference your brand guidelines file in the campaign brief JSON:

```json
{
  "campaign_id": "SPRING2026",
  "campaign_name": "Spring Collection",
  "brand_guidelines_file": "examples/guidelines/brand_custom_colors.yaml",
  "products": [...],
  ...
}
```

## Logo Placement

Control logo overlay on generated images:

```yaml
# Logo placement configuration
logo_placement: "bottom-right"      # Position: top-left, top-right, bottom-left, bottom-right
logo_clearspace: 30                 # Spacing from edges (pixels)
logo_min_size: 60                   # Minimum logo width (pixels)
logo_max_size: 250                  # Maximum logo width (pixels)
logo_opacity: 1.0                   # Transparency (0.0-1.0)
logo_scale: 0.15                    # Size as % of image width (0.05-0.5)
```

Reference logo in campaign brief:

```json
{
  "products": [
    {
      "product_id": "PRODUCT-001",
      "existing_assets": {
        "logo": "examples/assets/logos/brand-logo.png"
      }
    }
  ]
}
```

See `docs/LOGO_PLACEMENT.md` for complete guide.

## Example Files

| File | Description |
|------|-------------|
| `brand_no_shadow.yaml` | Clean design without drop shadows |
| `brand_custom_colors.yaml` | Custom brand colors for text (blue text + white shadow) |
| `brand_with_background.yaml` | Semi-transparent background box behind text |
| `brand_with_logo.yaml` | Standard logo placement configuration |
| `brand_logo_watermark.yaml` | Watermark-style semi-transparent logo |
| `brand_guidelines.md` | Full brand guidelines documentation for TechStyle |
| `localization_rules.yaml` | Localization and translation guidelines |

## Testing Different Styles

```bash
# Test clean design (no shadows)
./run_cli.sh examples/no_shadow_test.json

# Test custom brand colors
./run_cli.sh examples/text_customization_test.json

# Test background box overlay
./run_cli.sh examples/text_background_test.json

# Test default style (shadows enabled)
./run_cli.sh examples/campaign_brief.json
```

## Tips for Text Visibility

1. **Light backgrounds**: Use dark text or enable shadows
2. **Dark backgrounds**: Use light text or enable shadows
3. **Busy/colorful backgrounds**: Enable `text_background` with high opacity (0.7-0.8)
4. **Minimalist designs**: Disable shadows and use high-contrast text colors
5. **Brand alignment**: Match `text_color` to your brand's primary color palette

## Color Format

All colors must be in **hex format** with the `#` prefix:
- ✅ `"#0066FF"` (correct)
- ✅ `"#FFFFFF"` (correct)
- ❌ `"0066FF"` (missing #)
- ❌ `"rgb(0, 102, 255)"` (not supported)

## Opacity Range

`text_background_opacity` must be between **0.0** (fully transparent) and **1.0** (fully opaque):
- `0.3` - Very subtle background
- `0.5` - Balanced transparency (default)
- `0.7` - Strong background for busy images
- `1.0` - Solid background (no transparency)
