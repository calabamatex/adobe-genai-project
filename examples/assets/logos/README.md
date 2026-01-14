# Logo Assets

Place your brand logo files in this directory to use them in campaign assets.

## Supported Formats

- **PNG** (recommended - supports transparency)
- **JPEG/JPG**
- **GIF**
- **WebP**

## Recommended Specifications

### File Format
- **PNG with transparency** for best results
- Transparent background allows logo to blend naturally

### Size
- **Minimum**: 200x200 pixels
- **Recommended**: 500x500 pixels or larger
- **Maximum**: 2000x2000 pixels
- Higher resolution logos scale better to different sizes

### Aspect Ratio
- Square (1:1) works best
- Rectangular logos also supported (maintains aspect ratio)

### File Size
- Keep under 1 MB for performance
- Optimize PNG files for web

## Example Logo Files

Place your logos here with descriptive names:

```
examples/assets/logos/
├── techstyle-logo.png          # Main brand logo
├── techstyle-logo-white.png    # White version for dark backgrounds
├── techstyle-icon.png          # Icon-only version
└── client-brand-logo.png       # Client specific logo
```

## Using Logos in Campaigns

Reference the logo in your campaign brief's `existing_assets`:

```json
{
  "products": [
    {
      "product_id": "PRODUCT-001",
      "product_name": "My Product",
      "existing_assets": {
        "hero": "path/to/product.png",
        "logo": "examples/assets/logos/techstyle-logo.png"
      }
    }
  ]
}
```

## Logo Placement Configuration

Configure logo appearance in brand guidelines:

```yaml
# examples/guidelines/my_brand.yaml

# Logo placement
logo_placement: "bottom-right"      # top-left, top-right, bottom-left, bottom-right
logo_clearspace: 30                 # Spacing from edges (pixels)
logo_min_size: 60                   # Minimum width (pixels)
logo_max_size: 250                  # Maximum width (pixels)
logo_opacity: 1.0                   # Transparency (0.0=invisible, 1.0=opaque)
logo_scale: 0.12                    # Size as % of image width (0.05-0.5)
```

## Logo Placement Options

### Standard Placement
```yaml
logo_placement: "bottom-right"      # Default, non-intrusive
logo_opacity: 1.0                   # Fully visible
logo_scale: 0.15                    # 15% of image width
```

### Watermark Style
```yaml
logo_placement: "top-left"          # Corner watermark
logo_opacity: 0.3                   # Subtle, semi-transparent
logo_scale: 0.20                    # Larger for visibility
```

### Prominent Branding
```yaml
logo_placement: "top-right"         # Visible corner
logo_opacity: 1.0                   # Fully opaque
logo_scale: 0.25                    # 25% of image width
logo_clearspace: 40                 # More spacing
```

## Tips for Best Results

### Logo Design
- Use transparent background PNG
- Ensure good contrast for different backgrounds
- Include padding in the logo file itself
- Test on both light and dark images

### Placement
- **Bottom-right**: Default, works for most campaigns
- **Top-left**: Watermark style, non-intrusive
- **Top-right**: Visible but doesn't overlap CTA text
- **Bottom-left**: Alternative to bottom-right

### Sizing
- **Small logos** (scale: 0.10-0.15): Subtle branding
- **Medium logos** (scale: 0.15-0.20): Standard branding
- **Large logos** (scale: 0.20-0.30): Prominent branding

### Opacity
- **1.0 (100%)**: Standard, fully visible logo
- **0.7-0.9 (70-90%)**: Subtle, less distracting
- **0.3-0.5 (30-50%)**: Watermark effect
- **0.1-0.2 (10-20%)**: Very subtle background mark

## Testing Your Logo

Create a test campaign:

```bash
# 1. Place your logo file here
cp /path/to/your/logo.png examples/assets/logos/my-logo.png

# 2. Create test campaign JSON
# Reference logo in existing_assets

# 3. Run campaign
./run_cli.sh examples/my_logo_test.json
```

## Troubleshooting

**Logo not appearing:**
- Verify file path in `existing_assets` is correct
- Check that logo file exists at specified path
- Ensure logo file is readable (check permissions)

**Logo too small/large:**
- Adjust `logo_scale` (0.05-0.5)
- Check `logo_min_size` and `logo_max_size`
- Verify source logo resolution

**Logo position wrong:**
- Check `logo_placement` value (must be exact: "top-left", "top-right", "bottom-left", "bottom-right")
- Adjust `logo_clearspace` for edge spacing

**Logo not transparent:**
- Convert to PNG with transparency
- Ensure alpha channel is present
- Check that logo background is truly transparent

## Creating Test Logos

If you don't have a logo file, you can create a simple one:

1. **Online Tools**:
   - Canva (free)
   - LogoMakr
   - Adobe Express

2. **Design Software**:
   - Adobe Illustrator
   - Figma
   - Inkscape (free)

3. **Quick Text Logo**:
   - Create text in any image editor
   - Export as PNG with transparent background
   - Size at least 500x500 pixels

## Example Configurations

See example brand guidelines:
- `examples/guidelines/brand_with_logo.yaml` - Standard logo placement
- `examples/guidelines/brand_logo_watermark.yaml` - Watermark style
