"""
Pytest configuration and shared fixtures for test suite.
"""
import pytest
from datetime import datetime
from pathlib import Path
import json
import yaml


@pytest.fixture
def example_product():
    """Example product for testing."""
    return {
        "product_id": "TEST-PROD-001",
        "product_name": "Test Product",
        "product_description": "A test product for unit testing",
        "product_category": "Electronics",
        "key_features": ["Feature 1", "Feature 2", "Feature 3"],
        "generation_prompt": "professional product photo of test product"
    }


@pytest.fixture
def example_campaign_message():
    """Example campaign message for testing."""
    return {
        "locale": "en-US",
        "headline": "Test Headline",
        "subheadline": "Test Subheadline",
        "cta": "Test CTA"
    }


@pytest.fixture
def example_brief(example_product, example_campaign_message):
    """Example campaign brief for testing."""
    return {
        "campaign_id": "TEST-CAMPAIGN-001",
        "campaign_name": "Test Campaign",
        "brand_name": "Test Brand",
        "target_market": "North America",
        "target_audience": "Test audience",
        "campaign_message": example_campaign_message,
        "products": [example_product],
        "aspect_ratios": ["1:1", "9:16"],
        "output_formats": ["png"],
        "image_generation_backend": "firefly",
        "enable_localization": True,
        "target_locales": ["en-US", "es-MX"]
    }


@pytest.fixture
def mock_image_bytes():
    """Mock image bytes for testing."""
    from PIL import Image
    from io import BytesIO

    # Create a valid test image
    img = Image.new('RGB', (1024, 1024), color='blue')
    buf = BytesIO()
    img.save(buf, format='PNG')
    return buf.getvalue()


@pytest.fixture
def mock_firefly_response():
    """Mock Adobe Firefly API response."""
    return {
        "outputs": [
            {
                "image": {
                    "url": "https://example.com/generated-image.jpg"
                }
            }
        ]
    }


@pytest.fixture
def mock_openai_response():
    """Mock OpenAI DALL-E API response."""
    return {
        "data": [
            {
                "url": "https://example.com/dalle-image.png"
            }
        ]
    }


@pytest.fixture
def mock_gemini_response():
    """Mock Google Gemini API response."""
    return {
        "predictions": [
            {
                "bytesBase64Encoded": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=="
            }
        ]
    }


@pytest.fixture
def mock_claude_response():
    """Mock Anthropic Claude API response."""
    return {
        "id": "msg_123",
        "type": "message",
        "role": "assistant",
        "content": [
            {
                "type": "text",
                "text": '{"result": "test response"}'
            }
        ],
        "model": "claude-sonnet-4-20250514",
        "stop_reason": "end_turn",
        "usage": {
            "input_tokens": 100,
            "output_tokens": 50
        }
    }


@pytest.fixture
def brand_guidelines_text():
    """Example brand guidelines text for testing."""
    return """
    Brand Guidelines

    Primary Colors: #0066CC, #1A1A1A
    Secondary Colors: #FFFFFF, #F5F5F5

    Typography:
    Primary Font: Montserrat
    Secondary Font: Open Sans

    Brand Voice: Professional, innovative, customer-focused

    Photography Style: Clean, modern, minimalist product photography
    with natural lighting and neutral backgrounds.

    Logo Usage:
    - Minimum clearspace: 20px
    - Minimum size: 50px

    Prohibited Uses:
    - Do not use dark or busy backgrounds
    - Avoid cluttered compositions

    Approved Taglines:
    - "Innovation at Your Fingertips"
    - "Designed for Tomorrow"
    """


@pytest.fixture
def localization_rules_yaml():
    """Example localization rules in YAML format."""
    return """
    market_specific_rules:
      en-US:
        tone: casual
        formality: informal
        preferred_style: direct
      es-MX:
        tone: warm
        formality: formal
        preferred_style: respectful
      fr-CA:
        tone: professional
        formality: formal
        preferred_style: polite

    prohibited_terms:
      en-US:
        - cheap
        - discount
      es-MX:
        - barato
        - oferta
      fr-CA:
        - rabais

    translation_glossary:
      en-US:
        product: product
        quality: quality
      es-MX:
        product: producto
        quality: calidad
      fr-CA:
        product: produit
        quality: qualité

    tone_guidelines:
      en-US: "Be direct and clear, use active voice"
      es-MX: "Be warm and respectful, use formal pronouns"
      fr-CA: "Be professional and polite, maintain formal tone"

    cultural_considerations:
      en-US:
        - Emphasize innovation and convenience
        - Use conversational language
      es-MX:
        - Show respect for family values
        - Use formal address when appropriate
      fr-CA:
        - Respect bilingual nature
        - Use inclusive language
    """


@pytest.fixture
def brand_guidelines_model():
    """Example brand guidelines model for testing."""
    from src.models import ComprehensiveBrandGuidelines

    return ComprehensiveBrandGuidelines(
        source_file="test_guidelines.pdf",
        primary_colors=["#0066CC", "#1A1A1A"],
        secondary_colors=["#FFFFFF", "#F5F5F5"],
        primary_font="Montserrat",
        secondary_font="Open Sans",
        brand_voice="Professional, innovative, customer-focused",
        photography_style="Clean, modern, minimalist product photography",
        logo_clearspace=20,
        logo_min_size=50,
        prohibited_uses=["No dark backgrounds", "No cluttered compositions"],
        approved_taglines=["Innovation at Your Fingertips"]
    )


@pytest.fixture
def localization_guidelines_model():
    """Example localization guidelines model for testing."""
    from src.models import LocalizationGuidelines

    return LocalizationGuidelines(
        source_file="test_localization.yaml",
        supported_locales=["en-US", "es-MX", "fr-CA"],
        market_specific_rules={
            "en-US": {"tone": "casual", "formality": "informal"},
            "es-MX": {"tone": "warm", "formality": "formal"},
            "fr-CA": {"tone": "professional", "formality": "formal"}
        },
        prohibited_terms={
            "en-US": ["cheap", "discount"],
            "es-MX": ["barato", "oferta"]
        },
        translation_glossary={
            "en-US": {"product": "product"},
            "es-MX": {"product": "producto"}
        }
    )


@pytest.fixture
def temp_output_dir(tmp_path):
    """Temporary output directory for testing."""
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    return output_dir


@pytest.fixture
def mock_env_vars(monkeypatch):
    """Mock environment variables for testing."""
    monkeypatch.setenv("FIREFLY_API_KEY", "test-firefly-key")
    monkeypatch.setenv("FIREFLY_CLIENT_ID", "test-firefly-client")
    monkeypatch.setenv("OPENAI_API_KEY", "test-openai-key")
    monkeypatch.setenv("GEMINI_API_KEY", "test-gemini-key")
    monkeypatch.setenv("CLAUDE_API_KEY", "test-claude-key")
    monkeypatch.setenv("DEFAULT_IMAGE_BACKEND", "firefly")
