# Brand Guidelines System

> **Comprehensive guide to brand guidelines configuration, enforcement, and customization**

## Overview

The Brand Guidelines System ensures consistent brand identity across all generated marketing assets. It provides comprehensive control over visual elements including colors, typography, text styling, logo placement, and design principles.

---

## Table of Contents

- [Quick Start](#quick-start)
- [Complete Configuration Reference](#complete-configuration-reference)
- [Visual Elements](#visual-elements)
- [Text Customization](#text-customization)
- [Logo Placement](#logo-placement)
- [Design Principles](#design-principles)
- [File Formats](#file-formats)
- [Examples](#examples)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

---

## Quick Start

### 1. Create Brand Guidelines File

Create `my_brand_guidelines.yaml`:

```yaml
brand_name: "Your Brand"

# Core Brand Colors
primary_color: "#0066CC"      # Brand primary
secondary_color: "#FF6B00"    # Brand secondary
accent_color: "#00CC66"       # Accent highlights

# Typography
primary_font_family: "Helvetica Neue"
font_size: 48
font_weight: "bold"

# Text Appearance
text_color: "#FFFFFF"
text_shadow: true
text_shadow_color: "#000000"
text_background: false

# Logo Configuration
logo_placement: "bottom-right"
logo_scale: 0.15
logo_opacity: 1.0
```

### 2. Reference in Campaign

```json
{
  "campaign_id": "MY_CAMPAIGN",
  "brand_guidelines_file": "my_brand_guidelines.yaml",
  ...
}
```

### 3. Run Campaign

```bash
./run_cli.sh campaign.json
```

---

## Complete Configuration Reference

### Brand Identity

```yaml
# Basic Information
brand_name: "Brand Name"              # Your brand name
brand_tagline: "Your Tagline"         # Optional tagline
brand_description: "Description"      # Brand description
source_file: "path/to/file"          # Source file path (auto-set)
```

### Color Palette

```yaml
# Primary Colors
primary_color: "#0066CC"              # Main brand color
secondary_color: "#FF6B00"            # Secondary brand color
accent_color: "#00CC66"               # Accent/highlight color

# Additional Colors
primary_colors:                       # Multiple primary shades
  - "#0066CC"
  - "#0052A3"
  - "#003D7A"

secondary_colors:                     # Multiple secondary shades
  - "#FF6B00"
  - "#E65C00"
  - "#CC4D00"

accent_colors:                        # Multiple accent colors
  - "#00CC66"
  - "#00B359"
  - "#00994D"

# Text Colors
text_color: "#FFFFFF"                 # Default text color (hex)
text_shadow_color: "#000000"          # Text shadow color (hex)
text_background_color: "#000000"      # Background box color (hex)
```

**Color Format Requirements:**
- Must use hex format: `#RRGGBB`
- Case-insensitive: `#0066cc` or `#0066CC`
- Must include `#` prefix
- RGB/HSL not supported

### Typography

```yaml
# Font Configuration
primary_font_family: "Helvetica Neue" # Primary font
secondary_font_family: "Georgia"      # Secondary font
font_size: 48                         # Base font size (pixels)
font_weight: "bold"                   # Font weight (normal, bold, etc.)
line_height: 1.2                      # Line height multiplier

# Supported Font Weights
# - normal
# - bold
# - light
# - medium
# - semibold
# - black
```

**Font Availability:**
- System fonts always available
- Custom fonts require installation
- Fallback to system fonts if unavailable

### Text Styling

```yaml
# Text Appearance
text_color: "#FFFFFF"                 # Text color
text_shadow: true                     # Enable drop shadows
text_shadow_color: "#000000"          # Shadow color
text_shadow_offset: 0.01              # Shadow offset (% of image size)

# Background Box
text_background: false                # Enable background box
text_background_color: "#000000"      # Background color
text_background_opacity: 0.5          # Opacity (0.0-1.0)
text_background_padding: 20           # Padding around text (pixels)
```

**Shadow Offset Calculation:**
```
offset_pixels = min(image_width, image_height) * text_shadow_offset
default: min(1920, 1080) * 0.01 = 10.8 pixels
```

### Logo Configuration

```yaml
# Logo Placement
logo_placement: "bottom-right"        # Position on image
logo_clearspace: 30                   # Margin from edges (pixels)
logo_min_size: 60                     # Minimum width (pixels)
logo_max_size: 250                    # Maximum width (pixels)
logo_scale: 0.15                      # Size as % of image width (0.05-0.5)
logo_opacity: 1.0                     # Transparency (0.0-1.0)

# Logo Placement Options
# - top-left
# - top-right
# - bottom-left
# - bottom-right
# - center (not recommended)
```

**Logo Sizing Logic:**
```python
desired_width = image_width * logo_scale
final_width = clamp(desired_width, logo_min_size, logo_max_size)
```

### Photography Style

```yaml
# Visual Style Guidelines
photography_style: "lifestyle"        # Photography style
mood: "energetic"                     # Desired mood
lighting: "natural"                   # Lighting preference
composition: "rule-of-thirds"         # Composition rule

# Photography Styles
# - lifestyle: Real-world context
# - studio: Clean, controlled environment
# - editorial: Magazine-style
# - product: Product-focused
# - atmospheric: Mood-driven

# Mood Options
# - energetic, calm, professional, playful, sophisticated, minimal
```

### Design Principles

```yaml
# Design System
design_style: "modern"                # Overall design style
spacing_unit: 8                       # Base spacing unit (pixels)
border_radius: 8                      # Border radius (pixels)
use_grid: true                        # Grid-based layouts

# Design Styles
# - modern: Clean, contemporary
# - classic: Traditional, timeless
# - minimal: Simplified, essential
# - bold: Strong, impactful
# - elegant: Refined, sophisticated
```

---

## Visual Elements

### Color System

#### Primary Color Usage

**Purpose:** Main brand identifier, headlines, CTAs

**Best Practices:**
- Use for primary brand touchpoints
- Ensure sufficient contrast (WCAG AA: 4.5:1 minimum)
- Test on light and dark backgrounds

**Example:**
```yaml
primary_color: "#0066CC"              # Electric Blue
text_color: "#FFFFFF"                 # White for contrast
```

#### Secondary Color Usage

**Purpose:** Supporting elements, accents, hierarchy

**Best Practices:**
- Complement primary color
- Use for secondary CTAs
- Create visual hierarchy

**Example:**
```yaml
secondary_color: "#FF6B00"            # Vibrant Orange
# Works well with Electric Blue primary
```

#### Color Combinations

**High Contrast (Recommended):**
```yaml
# Dark background
text_color: "#FFFFFF"
text_shadow_color: "#000000"

# Light background
text_color: "#1A1A1A"
text_shadow_color: "#FFFFFF"
```

**Brand Colors:**
```yaml
# Use brand primary
text_color: "#0066CC"                 # Brand blue
text_shadow_color: "#FFFFFF"          # White shadow
text_background: true
text_background_color: "#000000"
text_background_opacity: 0.6
```

### Typography Hierarchy

#### Font Pairing

**Recommended Combinations:**

1. **Modern Professional:**
```yaml
primary_font_family: "Helvetica Neue"
secondary_font_family: "Georgia"
```

2. **Classic Elegant:**
```yaml
primary_font_family: "Garamond"
secondary_font_family: "Futura"
```

3. **Contemporary Bold:**
```yaml
primary_font_family: "Montserrat"
secondary_font_family: "Open Sans"
```

4. **Tech/Startup:**
```yaml
primary_font_family: "SF Pro"
secondary_font_family: "Inter"
```

#### Font Sizing

**Responsive Sizing:**
```yaml
# For 1920x1080 (16:9)
font_size: 72                         # Large, impactful

# For 1080x1920 (9:16)
font_size: 56                         # Adjusted for vertical

# For 1080x1080 (1:1)
font_size: 64                         # Balanced
```

**Text Length Considerations:**
- Short headlines (1-3 words): Larger fonts (72-96px)
- Medium headlines (4-6 words): Medium fonts (48-64px)
- Long headlines (7+ words): Smaller fonts (36-48px)

---

## Text Customization

### Text Color Options

#### White Text (Default)
```yaml
text_color: "#FFFFFF"
text_shadow: true
text_shadow_color: "#000000"
```

**Best For:**
- Dark or colorful backgrounds
- Lifestyle photography
- Product shots with dark products

#### Dark Text
```yaml
text_color: "#1A1A1A"
text_shadow: true
text_shadow_color: "#FFFFFF"
```

**Best For:**
- Light backgrounds
- Minimal designs
- Clean, bright product photography

#### Brand Color Text
```yaml
text_color: "#0066CC"                 # Brand blue
text_shadow: true
text_shadow_color: "#FFFFFF"
text_background: true
text_background_color: "#000000"
text_background_opacity: 0.7
```

**Best For:**
- Strong brand recognition
- Busy backgrounds (with background box)
- Differentiation from competitors

### Text Shadow Techniques

#### Standard Drop Shadow (Default)
```yaml
text_shadow: true
text_shadow_color: "#000000"
text_shadow_offset: 0.01
```

**Effect:** Classic shadow for depth

#### No Shadow (Minimal)
```yaml
text_shadow: false
```

**Best For:**
- Clean backgrounds
- Minimal design aesthetic
- High contrast situations

#### Reverse Shadow (Light on Dark)
```yaml
text_color: "#1A1A1A"
text_shadow: true
text_shadow_color: "#FFFFFF"
```

**Effect:** Light shadow on dark text

#### Heavy Shadow (Dramatic)
```yaml
text_shadow: true
text_shadow_color: "#000000"
text_shadow_offset: 0.02              # Double default
```

**Effect:** Strong, dramatic shadow

### Background Box Options

#### No Background (Default)
```yaml
text_background: false
```

**Best For:** Clean images with good contrast

#### Subtle Background
```yaml
text_background: true
text_background_color: "#000000"
text_background_opacity: 0.3
```

**Best For:** Slight readability boost

#### Balanced Background (Recommended)
```yaml
text_background: true
text_background_color: "#000000"
text_background_opacity: 0.5
```

**Best For:** General use, good readability

#### Strong Background
```yaml
text_background: true
text_background_color: "#000000"
text_background_opacity: 0.7
```

**Best For:** Busy backgrounds, maximum readability

#### Solid Background
```yaml
text_background: true
text_background_color: "#000000"
text_background_opacity: 1.0
```

**Best For:** Banner style, guaranteed readability

#### Brand Color Background
```yaml
text_color: "#FFFFFF"
text_background: true
text_background_color: "#0066CC"      # Brand blue
text_background_opacity: 0.8
```

**Effect:** Strong brand identity

---

## Logo Placement

### Placement Positions

#### Bottom-Right (Recommended)
```yaml
logo_placement: "bottom-right"
logo_clearspace: 30
```

**Best For:**
- Most layouts
- Standard practice
- Least intrusive

#### Bottom-Left
```yaml
logo_placement: "bottom-left"
logo_clearspace: 30
```

**Best For:**
- When CTA is bottom-right
- Balanced composition
- European markets

#### Top-Right
```yaml
logo_placement: "top-right"
logo_clearspace: 30
```

**Best For:**
- When headline is bottom-left
- Letterhead style
- Formal communications

#### Top-Left
```yaml
logo_placement: "top-left"
logo_clearspace: 30
```

**Best For:**
- Website/app mockups
- Navigation style layouts
- Tech products

### Logo Sizing Strategies

#### Small Logo (Subtle)
```yaml
logo_scale: 0.10                      # 10% of image width
logo_min_size: 50
logo_max_size: 150
```

**Best For:** High-end, luxury brands

#### Medium Logo (Balanced)
```yaml
logo_scale: 0.15                      # 15% of image width
logo_min_size: 60
logo_max_size: 200
```

**Best For:** Most brands (recommended)

#### Large Logo (Prominent)
```yaml
logo_scale: 0.20                      # 20% of image width
logo_min_size: 80
logo_max_size: 300
```

**Best For:** Brand awareness campaigns

#### Watermark Style
```yaml
logo_scale: 0.12
logo_opacity: 0.3                     # Semi-transparent
logo_placement: "bottom-right"
```

**Best For:** Subtle branding, photography

### Logo Clearspace

**Minimum Clearspace (Tight):**
```yaml
logo_clearspace: 20                   # 20 pixels
```

**Standard Clearspace (Recommended):**
```yaml
logo_clearspace: 30                   # 30 pixels
```

**Generous Clearspace (Luxury):**
```yaml
logo_clearspace: 50                   # 50 pixels
```

---

## Design Principles

### Visual Hierarchy

**Priority 1: Headline**
- Largest text
- Highest contrast
- Top third or center

**Priority 2: Subheadline**
- Medium text
- Supporting information
- Below headline

**Priority 3: CTA**
- Clear, actionable
- High contrast
- Bottom third or button

**Priority 4: Logo**
- Appropriate size (10-20% width)
- Non-intrusive placement
- Brand consistency

### Composition Rules

#### Rule of Thirds
```yaml
composition: "rule-of-thirds"
```

Place key elements at intersection points:
- Headlines: Top third
- Products: Center or lower third
- CTA: Bottom third
- Logo: Corners

#### Golden Ratio
```yaml
composition: "golden-ratio"
```

Use 1.618:1 ratio for element sizing and placement.

#### Center-Weighted
```yaml
composition: "center"
```

Focus on center of image (use sparingly).

### Whitespace Usage

**Minimal Whitespace:**
- Full-bleed images
- Text overlay directly on image
- Busy, energetic feel

**Balanced Whitespace:**
- Padding around text elements
- Breathing room for logo
- Professional, clean

**Generous Whitespace:**
- Large margins
- Minimal text overlay
- Luxury, high-end feel

---

## File Formats

### YAML Format (Recommended)

```yaml
brand_name: "Brand Name"
primary_color: "#0066CC"
text_color: "#FFFFFF"
```

**Advantages:**
- Human-readable
- Easy to edit
- Comments supported
- Hierarchical structure

### JSON Format

```json
{
  "brand_name": "Brand Name",
  "primary_color": "#0066CC",
  "text_color": "#FFFFFF"
}
```

**Advantages:**
- Machine-readable
- Strict syntax
- Wide tool support

### Markdown Format (AI-Parsed)

Create `brand_guidelines.md`:

```markdown
# Brand Guidelines

## Colors
- Primary: #0066CC
- Secondary: #FF6B00

## Typography
- Font: Helvetica Neue
- Size: 48px
```

**Advantages:**
- Documentation-friendly
- AI extracts structured data
- Human-readable

**Note:** Requires Claude API for parsing (automatic).

---

## Examples

### Example 1: Modern Tech Brand

```yaml
brand_name: "TechCorp"
primary_color: "#0066FF"
secondary_color: "#00FF88"
text_color: "#FFFFFF"
text_shadow: true
text_background: false
primary_font_family: "SF Pro"
font_size: 56
font_weight: "bold"
logo_placement: "bottom-right"
logo_scale: 0.15
photography_style: "studio"
design_style: "modern"
```

### Example 2: Luxury Fashion Brand

```yaml
brand_name: "Élégance"
primary_color: "#1A1A1A"
secondary_color: "#D4AF37"              # Gold
text_color: "#FFFFFF"
text_shadow: false
text_background: false
primary_font_family: "Didot"
font_size: 72
font_weight: "light"
logo_placement: "bottom-left"
logo_scale: 0.12
logo_opacity: 1.0
logo_clearspace: 50
photography_style: "editorial"
design_style: "elegant"
```

### Example 3: Energetic Sports Brand

```yaml
brand_name: "PowerFit"
primary_color: "#FF0044"
secondary_color: "#FFD700"
accent_color: "#00FF00"
text_color: "#FFFFFF"
text_shadow: true
text_shadow_color: "#000000"
text_background: true
text_background_color: "#FF0044"
text_background_opacity: 0.8
primary_font_family: "Impact"
font_size: 64
font_weight: "black"
logo_placement: "top-right"
logo_scale: 0.18
photography_style: "lifestyle"
design_style: "bold"
mood: "energetic"
```

### Example 4: Minimal Wellness Brand

```yaml
brand_name: "Serene"
primary_color: "#E8F4F8"
secondary_color: "#7FB3D5"
text_color: "#2C3E50"
text_shadow: false
text_background: true
text_background_color: "#FFFFFF"
text_background_opacity: 0.7
primary_font_family: "Avenir"
font_size: 42
font_weight: "light"
logo_placement: "bottom-right"
logo_scale: 0.10
logo_opacity: 0.8
photography_style: "atmospheric"
design_style: "minimal"
mood: "calm"
```

---

## Best Practices

### 1. Color Accessibility

**WCAG Contrast Requirements:**
- **AA (Minimum):** 4.5:1 for normal text, 3:1 for large text
- **AAA (Enhanced):** 7:1 for normal text, 4.5:1 for large text

**Test Contrast:**
```
White (#FFFFFF) on Blue (#0066CC) = 5.74:1 ✅ AA
Black (#000000) on Blue (#0066CC) = 3.66:1 ❌ Below AA
White (#FFFFFF) on Black (#000000) = 21:1 ✅ AAA
```

**Solution for Low Contrast:**
- Add text shadows
- Enable background box
- Adjust color lightness/darkness

### 2. Font Selection

**System Fonts (Always Available):**
- Arial, Helvetica, Times New Roman, Georgia
- Verdana, Courier, Trebuchet MS
- Impact, Comic Sans MS (use carefully)

**Web-Safe Fonts:**
- SF Pro (Apple)
- Segoe UI (Windows)
- Roboto (Android/Google)

**Custom Fonts:**
- Install system-wide
- Provide fallback fonts
- Test across platforms

### 3. Logo Guidelines

**DO:**
- Maintain aspect ratio
- Use transparent PNG
- Provide adequate clearspace
- Test at multiple sizes

**DON'T:**
- Stretch or distort logo
- Place over busy backgrounds without clearspace
- Make logo too small (<50px) or too large (>30% width)
- Use low-resolution logos

### 4. Text Overlay Tips

**For Dark/Colorful Backgrounds:**
```yaml
text_color: "#FFFFFF"
text_shadow: true
text_shadow_color: "#000000"
```

**For Light/Bright Backgrounds:**
```yaml
text_color: "#1A1A1A"
text_shadow: true
text_shadow_color: "#FFFFFF"
```

**For Busy/Complex Backgrounds:**
```yaml
text_color: "#FFFFFF"
text_background: true
text_background_color: "#000000"
text_background_opacity: 0.7
```

### 5. Responsive Considerations

**Aspect Ratio Adjustments:**

```yaml
# Square (1:1) - Balanced sizing
font_size: 64
logo_scale: 0.15

# Landscape (16:9) - Horizontal emphasis
font_size: 72
logo_scale: 0.12

# Portrait (9:16) - Vertical emphasis
font_size: 56
logo_scale: 0.18
```

---

## Troubleshooting

### Issue: Text Not Readable

**Problem:** Text blends into background

**Solutions:**
1. Enable text shadow
2. Add background box
3. Increase background opacity
4. Use higher contrast text color

```yaml
# Solution
text_shadow: true
text_background: true
text_background_opacity: 0.7
```

### Issue: Logo Too Small/Large

**Problem:** Logo not visible or overwhelming

**Solutions:**
1. Adjust `logo_scale` (0.05-0.30 range)
2. Set appropriate `logo_min_size` and `logo_max_size`
3. Check source logo resolution

```yaml
# Solution for too small
logo_scale: 0.18
logo_min_size: 80

# Solution for too large
logo_scale: 0.12
logo_max_size: 180
```

### Issue: Colors Not Matching Brand

**Problem:** Generated assets don't match brand identity

**Solutions:**
1. Use exact hex values from brand guidelines
2. Include `#` prefix in all hex colors
3. Test colors on actual images

```yaml
# Correct format
primary_color: "#0066CC"          # ✅

# Incorrect formats
primary_color: "0066CC"           # ❌ Missing #
primary_color: "rgb(0,102,204)"   # ❌ Not supported
```

### Issue: Font Not Applied

**Problem:** System using fallback font

**Solutions:**
1. Verify font is installed system-wide
2. Check exact font name (case-sensitive)
3. Provide fallback fonts

```yaml
# With fallback
primary_font_family: "Helvetica Neue, Helvetica, Arial, sans-serif"
```

### Issue: Text Shadow Too Strong/Weak

**Problem:** Shadow too prominent or barely visible

**Solutions:**
1. Adjust `text_shadow_offset` (0.005-0.03)
2. Change shadow color lightness
3. Disable shadow for minimal designs

```yaml
# Subtle shadow
text_shadow_offset: 0.008

# Strong shadow
text_shadow_offset: 0.02

# No shadow
text_shadow: false
```

---

## Integration with Pipeline

The brand guidelines system integrates automatically:

1. **Loading:** Guidelines loaded before image generation
2. **Parsing:** AI extracts structure from documents (PDF/MD)
3. **Application:** Applied to all text overlays and logo placements
4. **Validation:** Colors and values validated at load time
5. **Fallback:** System defaults used if guidelines missing

**Pipeline Flow:**
```
Campaign Brief → Load Brand Guidelines → Generate Hero Image
  → Apply Brand Colors/Fonts → Overlay Text with Brand Styling
  → Add Logo with Brand Placement → Save Branded Asset
```

---

## Related Documentation

- **[TEXT_CUSTOMIZATION.md](TEXT_CUSTOMIZATION.md)** - Detailed text styling guide
- **[LOGO_PLACEMENT.md](LOGO_PLACEMENT.md)** - Complete logo placement guide
- **[API.md](API.md)** - API reference for brand guidelines
- **[ARCHITECTURE.md](../ARCHITECTURE.md)** - System architecture

---

## Support

For questions about brand guidelines:
- Review example files in `examples/guidelines/`
- Check existing brand YAML files
- See TEXT_CUSTOMIZATION.md for text options
- See LOGO_PLACEMENT.md for logo options

---

## Summary

The Brand Guidelines System provides:

✅ **Complete color control** - Primary, secondary, accent colors
✅ **Typography management** - Fonts, sizes, weights
✅ **Text customization** - Colors, shadows, backgrounds
✅ **Logo placement** - 4-corner positioning with sizing
✅ **Design principles** - Composition, spacing, hierarchy
✅ **Multiple formats** - YAML, JSON, Markdown (AI-parsed)
✅ **Responsive sizing** - Adapts to aspect ratios
✅ **Accessibility** - WCAG contrast guidelines

**Ready to create brand-consistent marketing assets at scale.**
