# Logo Placement Guide

Complete guide to adding brand logos to your generated campaign images.

## Quick Start

### 1. Prepare Your Logo

- **Format**: PNG with transparent background (recommended)
- **Size**: 500x500 pixels or larger
- **Location**: `examples/assets/logos/your-logo.png`

### 2. Configure Brand Guidelines

```yaml
# examples/guidelines/my_brand.yaml
logo_placement: "bottom-right"      # Position
logo_clearspace: 30                 # Edge spacing
logo_scale: 0.15                    # 15% of image width
logo_opacity: 1.0                   # Fully opaque
```

### 3. Reference in Campaign

```json
{
  "products": [
    {
      "product_id": "PRODUCT-001",
      "existing_assets": {
        "logo": "examples/assets/logos/your-logo.png"
      }
    }
  ],
  "brand_guidelines_file": "examples/guidelines/my_brand.yaml"
}
```

### 4. Generate Campaign

```bash
./run_cli.sh examples/my_campaign.json
```

## Configuration Options

### logo_placement
**Type:** String
**Options:** `"top-left"`, `"top-right"`, `"bottom-left"`, `"bottom-right"`
**Default:** `"bottom-right"`

Position of logo on the image.

```yaml
logo_placement: "bottom-right"  # Default, non-intrusive
logo_placement: "top-left"      # Watermark style
logo_placement: "top-right"     # Visible but clear of text
logo_placement: "bottom-left"   # Alternative corner
```

### logo_clearspace
**Type:** Integer (pixels)
**Range:** Any positive number
**Default:** `20`

Minimum spacing from image edges.

```yaml
logo_clearspace: 20   # Tight spacing
logo_clearspace: 30   # Comfortable spacing (recommended)
logo_clearspace: 50   # Generous spacing
```

### logo_min_size
**Type:** Integer (pixels)
**Range:** Any positive number
**Default:** `50`

Minimum logo width. Logo won't be scaled below this size.

```yaml
logo_min_size: 50    # Small logos
logo_min_size: 80    # Medium visibility
logo_min_size: 120   # Large, prominent
```

### logo_max_size
**Type:** Integer (pixels)
**Range:** Any positive number
**Default:** `200`

Maximum logo width. Logo won't exceed this size even on large images.

```yaml
logo_max_size: 150   # Conservative sizing
logo_max_size: 200   # Standard (default)
logo_max_size: 300   # Allow larger logos
```

### logo_scale
**Type:** Float (percentage)
**Range:** `0.05` - `0.5` (5% - 50%)
**Default:** `0.15` (15%)

Logo size as percentage of image width.

```yaml
logo_scale: 0.10   # 10% - Subtle
logo_scale: 0.15   # 15% - Standard (default)
logo_scale: 0.20   # 20% - Prominent
logo_scale: 0.30   # 30% - Very large
```

### logo_opacity
**Type:** Float
**Range:** `0.0` - `1.0`
**Default:** `1.0` (fully opaque)

Logo transparency level.

```yaml
logo_opacity: 1.0    # Fully visible (default)
logo_opacity: 0.8    # Slightly transparent
logo_opacity: 0.5    # Semi-transparent
logo_opacity: 0.3    # Watermark effect
```

## Common Configurations

### 1. Standard Brand Logo
Clear, visible branding in bottom-right corner:

```yaml
logo_placement: "bottom-right"
logo_clearspace: 30
logo_min_size: 60
logo_max_size: 200
logo_opacity: 1.0
logo_scale: 0.15
```

### 2. Watermark Style
Subtle, semi-transparent watermark:

```yaml
logo_placement: "top-left"
logo_clearspace: 25
logo_min_size: 80
logo_max_size: 180
logo_opacity: 0.3              # 30% opacity
logo_scale: 0.18
```

### 3. Prominent Branding
Large, eye-catching logo:

```yaml
logo_placement: "top-right"
logo_clearspace: 40
logo_min_size: 100
logo_max_size: 300
logo_opacity: 1.0
logo_scale: 0.25               # 25% of image width
```

### 4. Minimal Footer Logo
Small, unobtrusive footer branding:

```yaml
logo_placement: "bottom-left"
logo_clearspace: 20
logo_min_size: 40
logo_max_size: 120
logo_opacity: 0.9
logo_scale: 0.10               # 10% of image width
```

### 5. Social Media Watermark
For user-generated content protection:

```yaml
logo_placement: "bottom-right"
logo_clearspace: 15
logo_min_size: 60
logo_max_size: 150
logo_opacity: 0.5              # Semi-transparent
logo_scale: 0.12
```

## Logo File Requirements

### Recommended Format
- **PNG with transparency** (alpha channel)
- Allows logo to blend naturally on any background
- No visible rectangle around logo

### Resolution
- **Minimum**: 200x200 pixels
- **Recommended**: 500x500 pixels
- **Optimal**: 1000x1000 pixels or larger
- Higher resolution = better quality at all sizes

### File Size
- Keep under 1 MB for performance
- Optimize PNG files (use tools like TinyPNG)
- Balance quality vs. file size

### Aspect Ratio
- Square (1:1) logos work best
- Rectangular logos maintain aspect ratio
- Very wide/tall logos may need larger `logo_scale`

## Sizing Logic

The system calculates logo size with this priority:

1. **Scale**: Logo width = `image_width × logo_scale`
2. **Constraints**: Enforce `logo_min_size` and `logo_max_size`
3. **Aspect Ratio**: Height calculated to maintain logo proportions
4. **Positioning**: Place at specified corner with `logo_clearspace`

**Example** (1920x1080 image, scale=0.15):
- Target width: 1920 × 0.15 = 288 pixels
- If max_size=200: Logo scaled to 200px width
- If logo is 500x300 (wider than tall): Height = 200 × (300/500) = 120px
- Final logo: 200x120 pixels

## Position Examples

Visual guide to placement options:

```
┌─────────────────────────┐
│ TL             TR       │  TL = top-left
│                         │  TR = top-right
│                         │  BL = bottom-left
│         Text            │  BR = bottom-right (default)
│       Overlays          │
│         Here            │
│                         │
│ BL             BR       │
└─────────────────────────┘
```

**Best Practices:**
- **bottom-right**: Default, doesn't conflict with typical text
- **top-left**: Watermark style, clear of text overlays
- **top-right**: Visible but text-safe
- **bottom-left**: Good alternative, less common

## Usage in Campaign Briefs

### Single Logo for All Products

```json
{
  "products": [
    {
      "product_id": "PRODUCT-001",
      "existing_assets": {
        "logo": "examples/assets/logos/brand-logo.png"
      }
    },
    {
      "product_id": "PRODUCT-002",
      "existing_assets": {
        "logo": "examples/assets/logos/brand-logo.png"
      }
    }
  ]
}
```

### Different Logos per Product

```json
{
  "products": [
    {
      "product_id": "TECH-001",
      "existing_assets": {
        "logo": "examples/assets/logos/tech-division.png"
      }
    },
    {
      "product_id": "HOME-001",
      "existing_assets": {
        "logo": "examples/assets/logos/home-division.png"
      }
    }
  ]
}
```

### Logo + Hero Image

```json
{
  "products": [
    {
      "product_id": "PRODUCT-001",
      "existing_assets": {
        "hero": "path/to/product-photo.png",
        "logo": "examples/assets/logos/brand-logo.png"
      }
    }
  ]
}
```

## Logo vs. Text Placement

Logos and text overlays work together:

```yaml
# Brand guidelines control both

# Logo in bottom-right
logo_placement: "bottom-right"
logo_clearspace: 30

# Text in bottom third (automatic)
# Text positioned at 65%, 77%, 88% from top
# Logo doesn't overlap text due to clearspace
```

**Avoiding Conflicts:**
- Text overlays: Bottom 35% of image
- Bottom logos: Should fit in bottom-right/bottom-left corners
- Clearspace prevents overlap
- Test on 9:16 (portrait) format for worst case

## Testing Your Logo

### Quick Test

```bash
# 1. Place logo
cp /path/to/logo.png examples/assets/logos/test-logo.png

# 2. Edit test campaign
# Update logo path in examples/logo_placement_test.json

# 3. Run test
./run_cli.sh examples/logo_placement_test.json

# 4. Check output
# Look in output/LOGO_TEST/
```

### Test Different Positions

Create multiple test configurations:

```bash
# Test each corner
./run_cli.sh examples/logo_test_top_left.json
./run_cli.sh examples/logo_test_top_right.json
./run_cli.sh examples/logo_test_bottom_left.json
./run_cli.sh examples/logo_test_bottom_right.json
```

### Test Different Sizes

```yaml
# Small logo test
logo_scale: 0.10
logo_max_size: 100

# Medium logo test
logo_scale: 0.15
logo_max_size: 200

# Large logo test
logo_scale: 0.25
logo_max_size: 300
```

## Troubleshooting

### Logo Not Appearing

**Check:**
1. Logo file path is correct in `existing_assets`
2. Logo file exists: `ls examples/assets/logos/your-logo.png`
3. File has read permissions
4. Brand guidelines file referenced in campaign
5. Check console output for error messages

**Fix:**
```bash
# Verify file exists
ls -lh examples/assets/logos/your-logo.png

# Check permissions
chmod 644 examples/assets/logos/your-logo.png
```

### Logo Too Small/Large

**Adjust scale:**
```yaml
# Make larger
logo_scale: 0.20        # Was 0.15
logo_max_size: 300      # Was 200

# Make smaller
logo_scale: 0.10        # Was 0.15
logo_min_size: 40       # Was 60
```

### Logo Not Transparent

**Solution:**
1. Convert logo to PNG with transparency
2. Use image editor (Photoshop, GIMP, Photopea)
3. Delete background layer
4. Export as PNG-24 or PNG-32

### Logo Position Wrong

**Check spelling:**
```yaml
# Correct options (case-sensitive)
logo_placement: "top-left"
logo_placement: "top-right"
logo_placement: "bottom-left"
logo_placement: "bottom-right"

# Wrong (won't work)
logo_placement: "topleft"       # Missing hyphen
logo_placement: "Top-Left"      # Wrong case
logo_placement: "right-bottom"  # Wrong order
```

### Logo Overlaps Text

**Increase clearspace:**
```yaml
logo_clearspace: 50     # More space from edges
```

**Or change position:**
```yaml
logo_placement: "top-left"  # Move away from text
```

### Logo Quality Poor

**Use higher resolution:**
- Source logo should be at least 500x500 pixels
- For large images (9:16 portrait), use 1000x1000+
- PNG format maintains quality better than JPEG

## Advanced Configuration

### Dynamic Sizing Based on Format

The logo automatically scales relative to image width, so it looks proportional on all aspect ratios:

- **1:1** (1024x1024): scale=0.15 → ~154px logo
- **9:16** (1080x1920): scale=0.15 → ~162px logo
- **16:9** (1920x1080): scale=0.15 → ~288px logo

### Opacity for Busy Backgrounds

```yaml
# Subtle logo on busy/colorful images
logo_opacity: 0.6
logo_placement: "top-left"
```

### Multiple Logo Versions

Use different logos for different contexts:

```yaml
# Light backgrounds
logo: "examples/assets/logos/logo-dark.png"

# Dark backgrounds
logo: "examples/assets/logos/logo-white.png"
```

## Examples Repository

**Brand Guidelines:**
- `examples/guidelines/brand_with_logo.yaml` - Standard placement
- `examples/guidelines/brand_logo_watermark.yaml` - Watermark style

**Test Campaigns:**
- `examples/logo_placement_test.json` - Basic logo test

**Assets:**
- `examples/assets/logos/README.md` - Logo requirements guide

## Related Documentation

- Text overlay customization: `docs/TEXT_CUSTOMIZATION.md`
- Brand guidelines: `examples/guidelines/README.md`
- Campaign creation: `docs/CAMPAIGN_GENERATOR.md`
