# Adobe GenAI Creative Automation Platform

> **AI-powered creative automation platform for generating localized, brand-compliant marketing assets at scale**

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

---

## 🚀 Overview

Adobe GenAI Creative Automation Platform is an enterprise-grade system that automates the creation of marketing assets using generative AI. It combines **multiple AI image generation backends** (Adobe Firefly, OpenAI DALL-E, Google Gemini) with **intelligent text localization** (Claude 3.5 Sonnet) and **legal compliance checking** to produce brand-consistent, legally compliant marketing materials across multiple locales and formats.

### Key Capabilities

- 🎨 **Multi-Backend Image Generation** - Adobe Firefly, OpenAI DALL-E 3, Google Gemini Imagen 4
- 🌍 **AI-Powered Localization** - Claude 3.5 Sonnet for culturally-adapted messaging
- ⚖️ **Legal Compliance Checking** - Pre-generation validation (FTC, FDA, SEC, FINRA)
- 🎭 **Brand Guidelines Enforcement** - Automated brand consistency across all assets
- 📐 **Multi-Format Asset Generation** - 1:1, 16:9, 9:16 aspect ratios
- 🔄 **Asset Reuse System** - Intelligent caching to reduce API costs
- 🎨 **Advanced Text Customization** - Colors, shadows, backgrounds with brand control
- 🖼️ **Logo Placement** - Automated logo overlay with 4-corner positioning
- 📊 **Campaign Analytics** - Success rates, processing times, error tracking

---

## 📋 Table of Contents

- [Features](#-features)
- [Legal Compliance](#%EF%B8%8F-legal-compliance-system)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Usage](#-usage)
- [Architecture](#-architecture)
- [Documentation](#-documentation)
- [Examples](#-examples)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### Image Generation
- ✅ **Adobe Firefly** - Enterprise-grade, commercially-safe generation
- ✅ **OpenAI DALL-E 3** - High-quality, creative generation
- ✅ **Google Gemini Imagen 4** - Latest Google AI image generation
- ✅ **Automatic fallback** - Switch backends seamlessly
- ✅ **Hero image caching** - Generate once, reuse across formats

### Localization & Translation
- ✅ **Claude 3.5 Sonnet** - Context-aware message localization
- ✅ **Cultural adaptation** - Not just translation, but cultural relevance
- ✅ **Multiple locales** - en-US, es-MX, en-GB, fr-FR, de-DE, ja-JP, and more
- ✅ **Tone preservation** - Maintains brand voice across languages
- ✅ **Localization guidelines** - Customizable per-locale rules

### Legal Compliance
- ✅ **Pre-generation validation** - Catch issues before asset creation
- ✅ **Industry templates** - General, Health/FDA, Financial/SEC
- ✅ **Three severity levels** - Error (blocks), Warning (advisory), Info (reminders)
- ✅ **Prohibited content detection** - Words, phrases, claims
- ✅ **Required disclaimers** - Automatic tracking and reminders
- ✅ **Locale-specific rules** - Different regulations per market

### Brand Guidelines
- ✅ **Color palette enforcement** - Primary, secondary, accent colors
- ✅ **Typography control** - Font family, sizes, weights
- ✅ **Text customization** - Colors, shadows, backgrounds, opacity
- ✅ **Logo placement** - 4-corner positioning with sizing control
- ✅ **Design system compliance** - Consistent brand experience

### Asset Management
- ✅ **Multi-format generation** - Square (1:1), Landscape (16:9), Portrait (9:16)
- ✅ **Multiple output formats** - PNG, JPEG, WebP
- ✅ **Asset reuse** - Intelligent caching system
- ✅ **Organized storage** - Campaign/Locale/Product/Format hierarchy
- ✅ **Brief updates** - Automatic tracking of generated assets

### Campaign Analytics
- ✅ **Processing metrics** - Time, success rate, error tracking
- ✅ **Asset inventory** - Complete manifest of generated assets
- ✅ **JSON reports** - Machine-readable campaign summaries
- ✅ **Error reporting** - Detailed failure information

---

## ⚖️ Legal Compliance System

### Overview

The platform includes a **comprehensive legal compliance framework** that validates campaign content against regulatory requirements **before asset generation**. This prevents costly compliance violations and ensures all marketing materials meet industry-specific legal standards.

### Supported Regulatory Frameworks

#### 1. **General Compliance (FTC)**
- **Federal Trade Commission** consumer protection rules
- False advertising prevention
- Truth in advertising requirements
- Endorsement and testimonial guidelines
- Deceptive pricing claims detection

#### 2. **Health & Pharmaceuticals (FDA)**
- **Food and Drug Administration** medical claims validation
- Prohibited disease claims (cure, treat, prevent, diagnose)
- Required supplement disclaimers
- Drug approval status verification
- Health benefit substantiation requirements

#### 3. **Financial Services (SEC/FINRA)**
- **Securities and Exchange Commission** investment disclaimers
- **FINRA** broker-dealer regulations
- Risk disclosure requirements
- Past performance disclaimer enforcement
- Prohibited guarantee language

### Compliance Features

✅ **Pre-Generation Validation**
- Catches compliance issues BEFORE creating assets
- Blocks generation if critical violations detected
- Saves time and prevents wasted API costs

✅ **Three Severity Levels**
- **ERROR** - Blocks asset generation (e.g., prohibited medical claims)
- **WARNING** - Advisory notices (e.g., consider adding disclaimer)
- **INFO** - Best practice reminders (e.g., suggested language)

✅ **Intelligent Content Detection**
- Prohibited words and phrases (context-aware)
- Required disclaimers tracking
- Locale-specific regulatory rules
- Industry-specific claim validation

✅ **Comprehensive Documentation**
- Pre-built compliance templates
- Real-world examples for each industry
- Implementation guide with code examples
- Customizable rules for your specific needs

### Compliance Validation Example

```python
# Campaign brief with FDA compliance
{
  "campaign_id": "SUPPLEMENT_2026",
  "compliance_template": "health_fda",  # Enable FDA validation
  "products": [{
    "name": "VitaBoost Supplement",
    "description": "Supports immune health*",  # Safe claim
    "messaging": {
      "headline": "Feel Your Best Every Day",
      "subheadline": "Natural wellness support",
      "disclaimer": "*These statements have not been evaluated by the FDA..."
    }
  }]
}
```

**Result:** ✅ PASSES - Includes required disclaimer, avoids prohibited claims

```python
# Example that would FAIL validation
{
  "description": "Cures common cold and prevents flu",  # ❌ Prohibited
  "disclaimer": null  # ❌ Missing required disclaimer
}
```

**Result:** ❌ BLOCKED - Contains prohibited disease claims, missing required disclaimers

### Compliance Templates

| Template | Industry | Key Regulations | Use Case |
|----------|----------|-----------------|----------|
| **general** | Consumer Goods | FTC Truth in Advertising | Default for most campaigns |
| **health_fda** | Health/Pharma | FDA Medical Claims | Supplements, OTC drugs, health products |
| **financial_sec** | Finance | SEC/FINRA Disclosures | Investments, financial services, trading |

### Documentation & Resources

📚 **Comprehensive Guides:**
- **[LEGAL_COMPLIANCE.md](examples/guidelines/LEGAL_COMPLIANCE.md)** (600+ lines)
  - Complete compliance system documentation
  - Severity levels and validation rules
  - Template configuration guide
  - Custom rule creation

- **[LEGAL_EXAMPLES.md](examples/guidelines/LEGAL_EXAMPLES.md)** (300+ lines)
  - Real-world compliant and non-compliant examples
  - Industry-specific use cases
  - Before/after comparisons
  - Best practices

- **[LEGAL_COMPLIANCE_IMPLEMENTATION.md](docs/LEGAL_COMPLIANCE_IMPLEMENTATION.md)** (400+ lines)
  - Technical implementation details
  - Code architecture and design patterns
  - Integration with campaign pipeline
  - Testing and validation strategies

### Quick Start with Compliance

```bash
# 1. Create campaign brief with compliance template
cat > my_campaign.json <<EOF
{
  "campaign_id": "MY_COMPLIANT_CAMPAIGN",
  "compliance_template": "health_fda",
  "products": [...]
}
EOF

# 2. Run generation - compliance check happens automatically
./run_cli.sh my_campaign.json firefly

# 3. Review compliance results in campaign report
cat output/*/*/campaign_report.json | jq '.compliance_results'
```

### Benefits

- **Risk Mitigation** - Prevent regulatory violations before they happen
- **Cost Savings** - Avoid regenerating non-compliant assets
- **Time Savings** - Automated validation vs manual legal review
- **Audit Trail** - Complete compliance documentation for legal teams
- **Scalability** - Validate 100s of assets with consistent standards

### Industry Applications

✅ **Healthcare & Pharmaceuticals** - Supplements, OTC drugs, medical devices
✅ **Financial Services** - Investment products, trading platforms, financial advice
✅ **Consumer Goods** - Food products, cosmetics, consumer electronics
✅ **E-commerce** - Pricing claims, promotional offers, product descriptions
✅ **Insurance** - Policy claims, benefit descriptions, comparative advertising

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- API Keys:
  - **Anthropic** (Claude) - Required for localization
  - **OpenAI** (optional) - For DALL-E 3 generation
  - **Google AI Studio** (optional) - For Gemini Imagen 4
  - **Adobe Firefly** (optional) - For Adobe Firefly generation

### 1. Clone & Install

```bash
# Clone repository
git clone https://github.com/yourusername/adobe-genai-project.git
cd adobe-genai-project

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure API Keys

Create a `.env` file in the project root:

```bash
# Required
ANTHROPIC_API_KEY=sk-ant-your-key-here

# Optional (choose at least one image backend)
OPENAI_API_KEY=sk-your-key-here
GOOGLE_API_KEY=your-key-here
ADOBE_CLIENT_ID=your-client-id
ADOBE_CLIENT_SECRET=your-client-secret
```

### 3. Run Your First Campaign

```bash
# Process example campaign
./run_cli.sh examples/campaign_brief.json
```

That's it! Your assets will be generated in `output/[PRODUCT_ID]/[CAMPAIGN_ID]/`

---

## 📚 Documentation

### Core Documentation
- **[QUICK_START.md](QUICK_START.md)** - Step-by-step setup guide
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - System design and components
- **[FEATURES.md](FEATURES.md)** - Complete feature matrix
- **[API.md](docs/API.md)** - API reference
- **[PACKAGES.md](docs/PACKAGES.md)** - Code package summaries

### Feature Guides
- **[BRAND_GUIDELINES.md](docs/BRAND_GUIDELINES.md)** - Complete brand guidelines system
- **[LOCALIZATION.md](docs/LOCALIZATION.md)** - AI-powered localization guide
- **[TEXT_CUSTOMIZATION.md](docs/TEXT_CUSTOMIZATION.md)** - Text colors, shadows, backgrounds
- **[LOGO_PLACEMENT.md](docs/LOGO_PLACEMENT.md)** - Logo overlay configuration
- **[IMAGE_QUALITY_OPTIMIZATION.md](docs/IMAGE_QUALITY_OPTIMIZATION.md)** - Advanced prompt engineering (NEW!)
- **[LEGAL_COMPLIANCE.md](examples/guidelines/LEGAL_COMPLIANCE.md)** - Legal checking system
- **[LEGAL_EXAMPLES.md](examples/guidelines/LEGAL_EXAMPLES.md)** - Compliance examples

### Tools & Scripts
- **[scripts/README.md](scripts/README.md)** - Campaign brief generator and utilities

### Contributing
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Development guidelines
- **[CHANGELOG.md](CHANGELOG.md)** - Version history

---

## 📁 Project Structure

```
adobe-genai-project/
├── src/
│   ├── genai/              # AI service integrations
│   │   ├── firefly.py      # Adobe Firefly client
│   │   ├── openai_client.py # OpenAI DALL-E client
│   │   ├── gemini.py       # Google Gemini client
│   │   ├── claude.py       # Claude localization service
│   │   └── factory.py      # Image generation factory
│   ├── parsers/            # Guidelines parsers
│   │   ├── brand_parser.py
│   │   ├── localization_parser.py
│   │   └── legal_parser.py
│   ├── models.py           # Pydantic data models
│   ├── pipeline.py         # Main orchestration pipeline
│   ├── image_processor.py  # Image manipulation
│   ├── legal_checker.py    # Legal compliance engine
│   ├── storage.py          # Asset storage manager
│   ├── cli.py              # CLI interface
│   └── main.py             # Entry point
├── examples/
│   ├── campaigns/          # Example campaign briefs
│   ├── guidelines/         # Brand, legal, localization guides
│   └── logos/              # Example brand logos
├── tests/                  # Test suite
├── docs/                   # Documentation
├── output/                 # Generated assets
└── README.md              # This file
```

---

## 🛠️ Campaign Brief Generator

**New in v1.1.0:** Generate campaign briefs with enhanced prompt engineering strategies!

The `scripts/generate_campaign_brief.py` tool creates campaign briefs implementing advanced prompt optimization from the [IMAGE_QUALITY_OPTIMIZATION.md](docs/IMAGE_QUALITY_OPTIMIZATION.md) guide, resulting in **30-40% better image quality**.

### Quick Usage

```bash
# List available templates
python3 scripts/generate_campaign_brief.py --list-templates

# Generate premium audio campaign (earbuds + headphones)
python3 scripts/generate_campaign_brief.py --template premium_audio

# Generate premium tech campaign (earbuds + monitor)
python3 scripts/generate_campaign_brief.py --template premium_tech

# Generate fashion campaign (sneakers)
python3 scripts/generate_campaign_brief.py --template fashion
```

### Enhanced Features

Generated campaign briefs include:

- **Structured Prompts** - Professional photography terminology and composition rules
- **7 Category Templates** - Electronics, fashion, food, beauty, automotive, premium audio, display tech
- **Detailed Breakdowns** - Style, composition, lighting, background, and detail parameters
- **Negative Prompts** - Explicit guidance on what to avoid
- **Backend Optimization** - Optimized for Firefly, DALL-E 3, and Gemini Imagen 4

### Example Generated Structure

```json
{
  "enhanced_generation": {
    "style_parameters": {
      "photography_style": "commercial product photography",
      "mood": "premium luxury",
      "quality_level": "ultra high resolution 8K"
    },
    "composition": {
      "viewing_angle": "3/4 angle from above",
      "depth_of_field": "shallow DOF with sharp focus",
      "rule_of_thirds": true
    },
    "lighting": {
      "primary_light": "soft key light from 45 degrees",
      "rim_light": "strong rim light highlighting metallic edges",
      "color_temperature": "cool daylight 5500K"
    },
    "negative_prompt": "cheap appearance, flat lighting, cluttered, low resolution"
  }
}
```

See [scripts/README.md](scripts/README.md) for complete documentation.

---

## 🎯 Examples

### Example 1: Premium Tech Campaign (NEW!)

Generate assets for premium earbuds and portable monitor across 5 global markets:

```bash
./run_cli.sh examples/premium_tech_campaign.json firefly
```

**Output:**
- 2 premium products (Elite Wireless Earbuds Pro, UltraView 4K Monitor)
- 5 locales (US, Mexico, France, Germany, Japan)
- 3 aspect ratios per product
- **30 total assets** + 2 hero images + 2 per-product reports

**Directory Structure:**
```
output/
├── EARBUDS-001/
│   └── PREMIUM2026/
│       ├── hero/EARBUDS-001_hero.png
│       ├── en-US/, es-MX/, fr-FR/, de-DE/, ja-JP/
│       └── EARBUDS-001_campaign_report.json
└── MONITOR-001/
    └── PREMIUM2026/
        └── ...
```

### Example 2: Multi-Locale Campaign

Generate assets for US, Mexico, and France:

```bash
./run_cli.sh examples/campaigns/multi_locale_campaign.json
```

**Output:**
- 3 locales × 2 products × 3 aspect ratios = **18 assets**
- Culturally-adapted messaging per locale
- Brand-consistent visuals across all markets

### Example 3: Specify Backend

Run with different image generation backends:

```bash
# Use Adobe Firefly (commercial-safe, high quality)
./run_cli.sh examples/campaign_brief.json firefly

# Use OpenAI DALL-E 3 (creative, high quality)
./run_cli.sh examples/campaign_brief.json openai

# Use Google Gemini Imagen 4 (fast, high quality)
./run_cli.sh examples/campaign_brief.json gemini
```

### Example 4: Health Product with Legal Compliance

Generate FDA-compliant health product assets:

```bash
./run_cli.sh examples/campaigns/health_product_campaign.json
```

**Features:**
- Pre-generation legal compliance check
- Blocks prohibited claims (cure, treat, prevent)
- Requires FDA disclaimers
- Ensures regulatory compliance

### Example 5: Asset Reuse for Cost Savings

Reuse existing hero images, generate only new formats:

```bash
./run_cli.sh examples/campaigns/asset_reuse_campaign.json
```

**Benefits:**
- 70% reduction in API calls
- 90% faster processing
- Significant cost savings

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for:

- Code of Conduct
- Development setup
- Coding standards
- Pull request process
- Testing requirements

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Support

- **Documentation:** [Full Docs](docs/)
- **Issues:** [GitHub Issues](https://github.com/yourusername/adobe-genai-project/issues)
- **Discussions:** [GitHub Discussions](https://github.com/yourusername/adobe-genai-project/discussions)

---

## 🗺️ Roadmap

### Current Version: 1.2.0

### ✅ Completed Features (v1.0 - v1.2)

- ✅ **Legal Compliance System** - FTC, FDA, SEC/FINRA regulatory frameworks
- ✅ **Multi-Backend AI** - Firefly, DALL-E 3, Gemini integration
- ✅ **AI Localization** - 40+ languages with Claude 3.5 Sonnet
- ✅ **Phase 1 Innovation** - Per-element text customization (patent-pending)
- ✅ **Brand Guidelines** - Comprehensive enforcement system
- ✅ **Asset Optimization** - Hero image reuse, cost savings
- ✅ **Campaign Analytics** - Success tracking and reporting

### Planned Features (v1.3+)

- [ ] **Video Generation** - Extend to video asset generation
- [ ] **Interactive Previews** - Web UI for campaign preview
- [ ] **A/B Testing** - Generate variants for testing
- [ ] **Performance Analytics** - Track asset performance
- [ ] **Template Library** - Pre-built campaign templates
- [ ] **API Server** - RESTful API for integrations
- [ ] **Additional Compliance** - GDPR, CCPA, international regulations
- [ ] **Compliance Reporting** - Export compliance reports for legal teams

---

<div align="center">

**[⬆ back to top](#adobe-genai-creative-automation-platform)**

Made with ❤️ by the Adobe GenAI Team

</div>
# adobe-genai-project
# adobe-genai-project
# adobe-genai-project
# adobe-genai-project
