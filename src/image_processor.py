"""Image processing for campaign assets."""
from PIL import Image, ImageDraw, ImageFont
from typing import Tuple, Optional
from io import BytesIO
from src.models import CampaignMessage, ComprehensiveBrandGuidelines


class ImageProcessor:
    """Process and manipulate campaign images."""
    
    def __init__(self):
        pass
    
    def resize_to_aspect_ratio(
        self,
        image_bytes: bytes,
        target_ratio: str
    ) -> Image.Image:
        """Resize image to target aspect ratio."""
        image = Image.open(BytesIO(image_bytes))
        
        ratio_map = {
            "1:1": (1024, 1024),
            "9:16": (1080, 1920),
            "16:9": (1920, 1080),
            "4:5": (1080, 1350)
        }
        
        target_size = ratio_map.get(target_ratio, (1024, 1024))
        
        # Calculate crop box to maintain aspect ratio
        img_ratio = image.width / image.height
        target_img_ratio = target_size[0] / target_size[1]
        
        if img_ratio > target_img_ratio:
            # Image is wider, crop width
            new_width = int(image.height * target_img_ratio)
            left = (image.width - new_width) // 2
            image = image.crop((left, 0, left + new_width, image.height))
        else:
            # Image is taller, crop height
            new_height = int(image.width / target_img_ratio)
            top = (image.height - new_height) // 2
            image = image.crop((0, top, image.width, top + new_height))
        
        # Resize to target
        return image.resize(target_size, Image.Resampling.LANCZOS)
    
    def apply_text_overlay(
        self,
        image: Image.Image,
        message: CampaignMessage,
        brand_guidelines: Optional[ComprehensiveBrandGuidelines] = None
    ) -> Image.Image:
        """Apply campaign message text overlay with smart text fitting."""
        # Create a copy
        img = image.copy()
        draw = ImageDraw.Draw(img)

        width, height = img.size

        # Use minimum dimension for base sizing to handle both portrait and landscape
        min_dimension = min(width, height)

        # Calculate initial font sizes based on minimum dimension
        # This ensures text fits in narrow formats like 9:16
        base_headline_size = int(min_dimension * 0.08)  # 8% of min dimension
        base_sub_size = int(min_dimension * 0.05)       # 5% of min dimension
        base_cta_size = int(min_dimension * 0.06)       # 6% of min dimension

        # Add margins (5% on each side)
        margin = int(width * 0.05)
        max_text_width = width - (2 * margin)

        # Calculate text positions (bottom third of image)
        y_headline = int(height * 0.65)
        y_subheadline = int(height * 0.77)
        y_cta = int(height * 0.88)

        # Get text colors from brand guidelines (defaults: white text, black shadow)
        text_color = "#FFFFFF"
        shadow_color = "#000000"
        use_shadow = True
        use_background = False
        bg_color = "#000000"
        bg_opacity = 0.5

        if brand_guidelines is not None:
            text_color = brand_guidelines.text_color
            shadow_color = brand_guidelines.text_shadow_color
            use_shadow = brand_guidelines.text_shadow
            use_background = brand_guidelines.text_background
            bg_color = brand_guidelines.text_background_color
            bg_opacity = brand_guidelines.text_background_opacity

        # Draw text with shadow and smart fitting
        texts = [
            (message.headline, y_headline, base_headline_size, "headline"),
            (message.subheadline, y_subheadline, base_sub_size, "subheadline"),
            (message.cta, y_cta, base_cta_size, "cta")
        ]

        for text, y_pos, initial_font_size, text_type in texts:
            # Find optimal font size that fits within max_text_width
            font, final_text = self._fit_text_to_width(
                text,
                initial_font_size,
                max_text_width,
                draw
            )

            # Calculate centered x position
            bbox = draw.textbbox((0, 0), final_text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x_pos = (width - text_width) // 2

            # Draw semi-transparent background box if enabled
            if use_background:
                padding = int(min_dimension * 0.02)  # 2% padding around text
                bg_x1 = x_pos - padding
                bg_y1 = y_pos - padding
                bg_x2 = x_pos + text_width + padding
                bg_y2 = y_pos + text_height + padding

                # Create semi-transparent overlay
                overlay = Image.new('RGBA', img.size, (0, 0, 0, 0))
                overlay_draw = ImageDraw.Draw(overlay)

                # Convert hex color to RGBA with opacity
                bg_rgb = tuple(int(bg_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
                bg_rgba = bg_rgb + (int(bg_opacity * 255),)

                overlay_draw.rectangle([bg_x1, bg_y1, bg_x2, bg_y2], fill=bg_rgba)
                img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
                draw = ImageDraw.Draw(img)

            # Draw shadow if enabled
            if use_shadow:
                shadow_offset = max(2, int(min_dimension * 0.01))
                draw.text((x_pos + shadow_offset, y_pos + shadow_offset), final_text, fill=shadow_color, font=font)

            # Draw text
            draw.text((x_pos, y_pos), final_text, fill=text_color, font=font)

        return img

    def _fit_text_to_width(
        self,
        text: str,
        initial_size: int,
        max_width: int,
        draw: ImageDraw.ImageDraw
    ) -> tuple:
        """
        Dynamically adjust font size to fit text within max_width.
        Returns (font, text) tuple.
        """
        font_size = initial_size
        min_font_size = 12  # Don't go below this

        # Try decreasing font size until text fits
        for size in range(initial_size, min_font_size - 1, -2):
            font = self._load_font(size)
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]

            if text_width <= max_width:
                return (font, text)

        # If still too large at min size, try wrapping text
        font = self._load_font(min_font_size)
        words = text.split()

        # Try to fit on one line with truncation as last resort
        if len(words) > 3:
            # For long text, try multi-line wrapping
            lines = self._wrap_text(text, font, max_width, draw)
            if len(lines) <= 2:  # Only use wrapping if it fits in 2 lines
                return (font, '\n'.join(lines))

        # Last resort: truncate with ellipsis
        truncated = text
        while len(truncated) > 5:
            bbox = draw.textbbox((0, 0), truncated + "...", font=font)
            if bbox[2] - bbox[0] <= max_width:
                return (font, truncated + "...")
            truncated = truncated[:-1]

        return (font, text)  # Give up and return original

    def _wrap_text(
        self,
        text: str,
        font: ImageFont.FreeTypeFont,
        max_width: int,
        draw: ImageDraw.ImageDraw
    ) -> list:
        """Wrap text into multiple lines that fit within max_width."""
        words = text.split()
        lines = []
        current_line = []

        for word in words:
            test_line = ' '.join(current_line + [word])
            bbox = draw.textbbox((0, 0), test_line, font=font)

            if bbox[2] - bbox[0] <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]

        if current_line:
            lines.append(' '.join(current_line))

        return lines

    def _load_font(self, size: int) -> ImageFont.FreeTypeFont:
        """Load a TrueType font with fallback to default."""
        # List of common fonts across platforms (in order of preference)
        font_paths = [
            # macOS
            "/System/Library/Fonts/Helvetica.ttc",
            "/System/Library/Fonts/SFNSDisplay.ttf",
            "/Library/Fonts/Arial.ttf",
            "/System/Library/Fonts/Supplemental/Arial.ttf",
            # Windows
            "C:/Windows/Fonts/arial.ttf",
            "C:/Windows/Fonts/calibri.ttf",
            # Linux
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        ]

        # Try each font path
        for font_path in font_paths:
            try:
                return ImageFont.truetype(font_path, size)
            except (IOError, OSError):
                continue

        # If no system font found, use PIL's default but at larger size
        # Note: load_default() doesn't support size, so we try truetype with common names
        try:
            return ImageFont.truetype("Arial", size)
        except:
            pass

        try:
            return ImageFont.truetype("Helvetica", size)
        except:
            pass

        # Last resort: use default font (will be small)
        print(f"⚠️  Could not load TrueType font, using default (text may be small)")
        return ImageFont.load_default()

    def apply_logo_overlay(
        self,
        image: Image.Image,
        logo_path: str,
        brand_guidelines: Optional[ComprehensiveBrandGuidelines] = None
    ) -> Image.Image:
        """
        Apply logo overlay to image with positioning and sizing based on brand guidelines.

        Args:
            image: Base image to add logo to
            logo_path: Path to logo file
            brand_guidelines: Brand guidelines with logo placement settings

        Returns:
            Image with logo overlay applied
        """
        try:
            # Load logo
            logo = Image.open(logo_path)

            # Convert logo to RGBA if not already
            if logo.mode != 'RGBA':
                logo = logo.convert('RGBA')

            # Get brand guidelines settings (with defaults)
            placement = "bottom-right"
            clearspace = 20
            min_size = 50
            max_size = 200
            opacity = 1.0
            scale = 0.15  # 15% of image width by default

            if brand_guidelines is not None:
                placement = brand_guidelines.logo_placement
                clearspace = brand_guidelines.logo_clearspace
                min_size = brand_guidelines.logo_min_size
                max_size = brand_guidelines.logo_max_size
                opacity = brand_guidelines.logo_opacity
                scale = brand_guidelines.logo_scale

            # Calculate target logo width based on image width and scale
            target_width = int(image.width * scale)

            # Enforce min/max size constraints
            target_width = max(min_size, min(max_size, target_width))

            # Calculate target height maintaining aspect ratio
            aspect_ratio = logo.height / logo.width
            target_height = int(target_width * aspect_ratio)

            # Resize logo
            logo_resized = logo.resize((target_width, target_height), Image.Resampling.LANCZOS)

            # Apply opacity if needed
            if opacity < 1.0:
                # Create a copy with adjusted alpha channel
                logo_with_opacity = logo_resized.copy()
                alpha = logo_with_opacity.getchannel('A')
                alpha = alpha.point(lambda p: int(p * opacity))
                logo_with_opacity.putalpha(alpha)
                logo_resized = logo_with_opacity

            # Calculate position based on placement setting
            x, y = self._calculate_logo_position(
                image.size,
                logo_resized.size,
                placement,
                clearspace
            )

            # Convert base image to RGBA for compositing
            if image.mode != 'RGBA':
                image = image.convert('RGBA')

            # Create a transparent layer for the logo
            logo_layer = Image.new('RGBA', image.size, (0, 0, 0, 0))
            logo_layer.paste(logo_resized, (x, y), logo_resized)

            # Composite logo onto image
            result = Image.alpha_composite(image, logo_layer)

            # Convert back to RGB
            return result.convert('RGB')

        except FileNotFoundError:
            print(f"⚠️  Logo file not found: {logo_path}")
            return image
        except Exception as e:
            print(f"⚠️  Error applying logo overlay: {e}")
            return image

    def _calculate_logo_position(
        self,
        image_size: Tuple[int, int],
        logo_size: Tuple[int, int],
        placement: str,
        clearspace: int
    ) -> Tuple[int, int]:
        """
        Calculate logo position based on placement setting.

        Args:
            image_size: (width, height) of base image
            logo_size: (width, height) of logo
            placement: "top-left", "top-right", "bottom-left", "bottom-right"
            clearspace: Minimum spacing from edges in pixels

        Returns:
            (x, y) coordinates for logo placement
        """
        img_width, img_height = image_size
        logo_width, logo_height = logo_size

        # Calculate positions for each corner
        positions = {
            "top-left": (clearspace, clearspace),
            "top-right": (img_width - logo_width - clearspace, clearspace),
            "bottom-left": (clearspace, img_height - logo_height - clearspace),
            "bottom-right": (img_width - logo_width - clearspace, img_height - logo_height - clearspace)
        }

        # Default to bottom-right if invalid placement
        return positions.get(placement.lower(), positions["bottom-right"])
