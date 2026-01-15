# API Documentation

## CLI Interface

### Commands

#### `process`
Process a campaign brief and generate assets.

```bash
python -m src.cli process --brief <path> [--backend <name>] [--verbose] [--dry-run]
```

**Arguments:**
- `--brief` (required) - Path to campaign brief JSON file
- `--backend` (optional) - Image generation backend (firefly, openai, gemini)
- `--verbose` (optional) - Enable verbose output
- `--dry-run` (optional) - Validate only, don't generate

**Example:**
```bash
python -m src.cli process --brief campaign.json --backend openai --verbose
```

---

## Python API

### CreativeAutomationPipeline

Main orchestrator for campaign processing.

```python
from src.pipeline import CreativeAutomationPipeline
from src.models import CampaignBrief

pipeline = CreativeAutomationPipeline(image_backend="openai")
result = await pipeline.process_campaign(brief)
```

#### `__init__(image_backend: str = None)`
Initialize pipeline with optional default backend.

#### `async process_campaign(brief: CampaignBrief, brief_path: str = None) -> CampaignOutput`
Process complete campaign.

**Parameters:**
- `brief` - Campaign brief model
- `brief_path` - Optional path for backup/updates

**Returns:** `CampaignOutput` with generated assets and metrics

---

### Image Generation Services

#### FireflyImageService

```python
from src.genai.firefly import FireflyImageService

service = FireflyImageService()
image_bytes = await service.generate_image(
    prompt="product photo",
    size="2048x2048",
    brand_guidelines=guidelines
)
```

#### OpenAIImageService

```python
from src.genai.openai_client import OpenAIImageService

service = OpenAIImageService()
image_bytes = await service.generate_image(
    prompt="product photo",
    size="1024x1024",
    brand_guidelines=guidelines
)
```

#### GeminiImageService

```python
from src.genai.gemini import GeminiImageService

service = GeminiImageService()
image_bytes = await service.generate_image(
    prompt="product photo",
    size="2048x2048",
    brand_guidelines=guidelines
)
```

---

### Claude Service

```python
from src.genai.claude import ClaudeService

service = ClaudeService()

# Localize message
localized = await service.localize_message(
    message=campaign_message,
    target_locale="es-MX",
    guidelines=localization_guidelines
)

# Extract brand guidelines
guidelines = await service.extract_brand_guidelines(
    file_path="brand.pdf"
)
```

---

### Image Processor

```python
from src.image_processor import ImageProcessor
from PIL import Image

processor = ImageProcessor()

# Resize to aspect ratio
resized = processor.resize_to_aspect_ratio(
    image_bytes=hero_image,
    aspect_ratio="16:9"
)

# Apply text overlay
with_text = processor.apply_text_overlay(
    image=resized,
    message=campaign_message,
    brand_guidelines=guidelines
)

# Apply logo overlay
final = processor.apply_logo_overlay(
    image=with_text,
    logo_path="logo.png",
    brand_guidelines=guidelines
)
```

---

### Legal Compliance Checker

```python
from src.legal_checker import LegalComplianceChecker
from src.models import LegalComplianceGuidelines

# Initialize checker
checker = LegalComplianceChecker(legal_guidelines)

# Check content
is_compliant, violations = checker.check_content(
    message=campaign_message,
    product_content={"description": "..."},
    locale="en-US"
)

# Generate report
report = checker.generate_report()

# Get summary
summary = checker.get_violation_summary()
# Returns: {"errors": 2, "warnings": 1, "info": 3}
```

---

### Storage Manager

```python
from src.storage import StorageManager

storage = StorageManager(output_dir="output")

# Get asset path (directories created automatically)
path = storage.get_asset_path(
    campaign_id="CAMPAIGN-001",
    locale="en-US",
    product_id="PROD-001",
    aspect_ratio="16:9",
    output_format="png"
)

# Save image
storage.save_image(image, path)

# Save per-product report
report_path = storage.save_report(
    campaign_output=output,
    campaign_id="CAMPAIGN-001",
    product_id="PROD-001"
)

# Backup brief
backup_path = storage.backup_campaign_brief("campaign.json")

# Update brief
storage.update_campaign_brief("campaign.json", output, hero_images)
```

---

## Data Models

### CampaignBrief

```python
from src.models import CampaignBrief

brief = CampaignBrief(
    campaign_id="SUMMER2026",
    campaign_name="Summer Campaign",
    brand_name="Brand",
    campaign_message=message,
    products=[product1, product2],
    target_locales=["en-US", "es-MX"],
    aspect_ratios=["1:1", "16:9", "9:16"],
    output_formats=["png"],
    brand_guidelines_file="brand.yaml",
    localization_guidelines_file="locale.yaml",
    legal_compliance_file="legal.yaml"
)
```

### Product

```python
from src.models import Product

product = Product(
    product_id="PROD-001",
    product_name="Product Name",
    product_description="Description",
    product_category="Category",
    key_features=["Feature 1", "Feature 2"],
    generation_prompt="product photo",
    existing_assets={
        "hero": "path/to/hero.png",
        "en-US_16:9": "path/to/asset.png"
    }
)
```

### ComprehensiveBrandGuidelines

```python
from src.models import ComprehensiveBrandGuidelines

guidelines = ComprehensiveBrandGuidelines(
    brand_name="Brand",
    primary_color="#0066CC",
    secondary_color="#FF6B00",
    text_color="#FFFFFF",
    text_shadow=True,
    text_shadow_color="#000000",
    text_background=False,
    text_background_color="#000000",
    text_background_opacity=0.5,
    logo_placement="bottom-right",
    logo_scale=0.15,
    logo_opacity=1.0
)
```

### LegalComplianceGuidelines

```python
from src.models import LegalComplianceGuidelines

legal = LegalComplianceGuidelines(
    source_file="legal.yaml",
    prohibited_words=["guarantee", "cure"],
    prohibited_phrases=["100% effective"],
    prohibited_claims=["scientifically proven"],
    restricted_terms={"natural": ["100%"]},
    required_disclaimers={"general": "Results may vary"},
    industry_regulations=["FTC", "FDA"]
)
```

---

## Error Handling

### APIError

Raised when external API calls fail.

```python
from src.genai.exceptions import APIError

try:
    image = await service.generate_image(prompt)
except APIError as e:
    print(f"API error: {e.message}")
    print(f"Status code: {e.status_code}")
```

### ValidationError

Raised when input validation fails (Pydantic).

```python
from pydantic import ValidationError

try:
    brief = CampaignBrief(**data)
except ValidationError as e:
    print(f"Validation errors: {e.errors()}")
```

### LegalComplianceError

Raised when legal compliance check fails.

```python
try:
    await pipeline.process_campaign(brief)
except Exception as e:
    if "Legal compliance check failed" in str(e):
        # Handle compliance failure
        pass
```

---

## External API Integration

### Anthropic Claude API

**Endpoint:** `https://api.anthropic.com/v1/messages`

```python
import anthropic

client = anthropic.Anthropic(api_key=api_key)

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=4096,
    messages=[{
        "role": "user",
        "content": prompt
    }]
)
```

### OpenAI API

**Endpoint:** `https://api.openai.com/v1/images/generations`

```python
import openai

response = openai.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1
)
```

### Google Gemini API

**Endpoint:** `https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict`

```python
import google.generativeai as genai

genai.configure(api_key=api_key)

model = genai.GenerativeModel('imagen-4.0-generate-001')
response = model.generate_images(
    prompt=prompt,
    number_of_images=1
)
```

---

## Configuration

### Environment Variables

```bash
# Required
ANTHROPIC_API_KEY=sk-ant-...

# Image backends (at least one)
OPENAI_API_KEY=sk-...
GOOGLE_API_KEY=...
ADOBE_CLIENT_ID=...
ADOBE_CLIENT_SECRET=...

# Optional
DEFAULT_IMAGE_BACKEND=openai
LOG_LEVEL=INFO
OUTPUT_DIR=output
MAX_CONCURRENT_REQUESTS=5
```

---

## Examples

See `examples/` directory for:
- Campaign briefs
- Brand guidelines
- Legal compliance templates
- Localization rules
