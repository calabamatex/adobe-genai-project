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

    # Text overlay customization
    text_shadow: bool = Field(default=True, description="Enable drop shadow on text overlays")
    text_color: str = Field(default="#FFFFFF", description="Text overlay color (hex)")
    text_shadow_color: str = Field(default="#000000", description="Text shadow color (hex)")
    text_background: bool = Field(default=False, description="Enable semi-transparent background box behind text")
    text_background_color: str = Field(default="#000000", description="Text background box color (hex)")
    text_background_opacity: float = Field(default=0.5, ge=0.0, le=1.0, description="Text background opacity (0.0-1.0)")

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
                "success_rate": 0.95
            }
        }
