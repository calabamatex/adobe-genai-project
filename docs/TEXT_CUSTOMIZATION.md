# Text Overlay Customization Guide

Complete guide to customizing text appearance in generated campaign images.

## Quick Start

Add text customization to your brand guidelines YAML file:

```yaml
# examples/guidelines/my_brand.yaml
source_file: "examples/guidelines/my_brand.yaml"

primary_colors:
  - "#0066FF"  # Your brand color

# Text overlay settings
text_color: "#0066FF"              # Use brand color for text
text_shadow: false                 # Disable shadows for clean look
text_background: false             # No background box
```

Reference in campaign brief:

```json
{
  "campaign_id": "MY_CAMPAIGN",
  "brand_guidelines_file": "examples/guidelines/my_brand.yaml",
  ...
}
```

## All Available Options

### Text Color
**Field:** `text_color`
**Type:** String (hex color)
**Default:** `"#FFFFFF"` (white)
**Description:** Main text color for headline, subheadline, and CTA

```yaml
text_color: "#0066FF"  # Electric blue
```

### Text Shadow
**Field:** `text_shadow`
**Type:** Boolean
**Default:** `true`
**Description:** Enable/disable drop shadow behind text

```yaml
text_shadow: false  # Clean, no-shadow design
```

### Shadow Color
**Field:** `text_shadow_color`
**Type:** String (hex color)
**Default:** `"#000000"` (black)
**Description:** Color of the drop shadow (when shadows enabled)

```yaml
text_shadow_color: "#FFFFFF"  # White shadow
```

### Text Background Box
**Field:** `text_background`
**Type:** Boolean
**Default:** `false`
**Description:** Enable semi-transparent background box behind text

```yaml
text_background: true  # Modern overlay style
```

### Background Color
**Field:** `text_background_color`
**Type:** String (hex color)
**Default:** `"#000000"` (black)
**Description:** Color of background box (when background enabled)

```yaml
text_background_color: "#1A1A1A"  # Dark gray
```

### Background Opacity
**Field:** `text_background_opacity`
**Type:** Float (0.0 - 1.0)
**Default:** `0.5`
**Description:** Transparency of background box (0=transparent, 1=opaque)

```yaml
text_background_opacity: 0.7  # 70% opaque
```

## Common Configurations

### 1. Default (High Contrast)
Best for general use with maximum visibility:

```yaml
text_color: "#FFFFFF"
text_shadow: true
text_shadow_color: "#000000"
text_background: false
```

### 2. Clean Minimalist
For bright, minimalist backgrounds:

```yaml
text_color: "#FFFFFF"
text_shadow: false
text_background: false
```

### 3. Brand Color Text
Use your brand colors:

```yaml
text_color: "#0066FF"        # Brand blue
text_shadow: true
text_shadow_color: "#FFFFFF" # White shadow for contrast
text_background: false
```

### 4. Modern Overlay Box
For busy or colorful backgrounds:

```yaml
text_color: "#FFFFFF"
text_shadow: false               # Shadow not needed with box
text_background: true
text_background_color: "#000000"
text_background_opacity: 0.7
```

### 5. Subtle Background
Light background effect:

```yaml
text_color: "#FFFFFF"
text_shadow: false
text_background: true
text_background_color: "#1A1A1A"
text_background_opacity: 0.3     # Very subtle
```

## Design Recommendations

### For Light Backgrounds
- Use dark text colors or enable shadows
- Example: White text with black shadow

### For Dark Backgrounds
- Use light text colors
- Consider white or light-colored shadows
- Example: White text with subtle shadow

### For Busy/Colorful Backgrounds
- Enable `text_background` with 0.6-0.8 opacity
- Disable shadows (not needed with background box)
- Use white text on dark semi-transparent box

### For Brand-Aligned Designs
- Use `text_color` matching your brand primary color
- Add contrasting shadow color
- Example: Blue brand text with white shadow

### For Modern, Clean Aesthetics
- Disable shadows (`text_shadow: false`)
- Use high-contrast text color
- Ensure background is clean/minimal

## Testing Your Configuration

```bash
# Create test campaign with your brand guidelines
./run_cli.sh examples/my_test_campaign.json

# Compare different styles
./run_cli.sh examples/no_shadow_test.json           # Clean design
./run_cli.sh examples/text_customization_test.json  # Brand colors
./run_cli.sh examples/text_background_test.json     # Background box
```

## Technical Details

### Text Positioning
- **Headline:** 65% from top
- **Subheadline:** 77% from top
- **CTA:** 88% from top
- **Alignment:** Center-aligned
- **Margins:** 5% on each side

### Font Sizing
- Calculated dynamically based on minimum image dimension
- **Headline:** 8% of min(width, height)
- **Subheadline:** 5% of min(width, height)
- **CTA:** 6% of min(width, height)
- Automatically reduces if text doesn't fit

### Shadow Offset
- Calculated as 1% of minimum image dimension
- Minimum: 2 pixels
- Applied diagonally (right + down)

### Background Box Padding
- 2% of minimum image dimension around text
- Applied to all sides

## Color Format Requirements

✅ **Correct:**
```yaml
text_color: "#0066FF"
text_shadow_color: "#FFFFFF"
text_background_color: "#1A1A1A"
```

❌ **Incorrect:**
```yaml
text_color: "0066FF"          # Missing #
text_color: "rgb(0,102,255)"  # Wrong format
text_color: "blue"            # Not hex
```

## Troubleshooting

**Text not visible:**
- Enable shadows or background box
- Increase `text_background_opacity`
- Use higher contrast text color

**Text color not applied:**
- Verify hex format includes `#` prefix
- Check YAML syntax (proper indentation)
- Ensure brand guidelines file is referenced in campaign brief

**Background box not showing:**
- Verify `text_background: true`
- Check that opacity is > 0
- Ensure color is valid hex format

**Shadow not appearing:**
- Verify `text_shadow: true`
- Check that text and shadow colors are different
- Ensure shadow color has valid hex format

## Examples Repository

All example files are in `/examples/guidelines/`:

- `brand_no_shadow.yaml` - Clean design
- `brand_custom_colors.yaml` - Brand color text
- `brand_with_background.yaml` - Background overlay
- `README.md` - Complete documentation

Test campaigns in `/examples/`:

- `no_shadow_test.json`
- `text_customization_test.json`
- `text_background_test.json`

## Support

For issues or questions:
- Check `/examples/guidelines/README.md`
- Review example configurations
- Verify YAML syntax and hex color formats
