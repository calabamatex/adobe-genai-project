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

That's it! Your assets will be generated in `output/[CAMPAIGN_ID]/`

---

## 📚 Documentation

### Core Documentation
- **[QUICK_START.md](QUICK_START.md)** - Step-by-step setup guide
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - System design and components
- **[FEATURES.md](FEATURES.md)** - Complete feature matrix
- **[API.md](docs/API.md)** - API reference
- **[PACKAGES.md](docs/PACKAGES.md)** - Code package summaries

### Feature Guides
- **[TEXT_CUSTOMIZATION.md](docs/TEXT_CUSTOMIZATION.md)** - Text colors, shadows, backgrounds
- **[LOGO_PLACEMENT.md](docs/LOGO_PLACEMENT.md)** - Logo overlay configuration
- **[LEGAL_COMPLIANCE.md](examples/guidelines/LEGAL_COMPLIANCE.md)** - Legal checking system
- **[LEGAL_EXAMPLES.md](examples/guidelines/LEGAL_EXAMPLES.md)** - Compliance examples

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

## 🎯 Examples

### Example 1: Multi-Locale Campaign

Generate assets for US, Mexico, and France:

```bash
./run_cli.sh examples/campaigns/multi_locale_campaign.json
```

**Output:**
- 3 locales × 2 products × 3 aspect ratios = **18 assets**
- Culturally-adapted messaging per locale
- Brand-consistent visuals across all markets

### Example 2: Health Product with Legal Compliance

Generate FDA-compliant health product assets:

```bash
./run_cli.sh examples/campaigns/health_product_campaign.json
```

**Features:**
- Pre-generation legal compliance check
- Blocks prohibited claims (cure, treat, prevent)
- Requires FDA disclaimers
- Ensures regulatory compliance

### Example 3: Asset Reuse for Cost Savings

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

### Current Version: 1.0.0

### Planned Features

- [ ] **Video Generation** - Extend to video asset generation
- [ ] **Interactive Previews** - Web UI for campaign preview
- [ ] **A/B Testing** - Generate variants for testing
- [ ] **Performance Analytics** - Track asset performance
- [ ] **Template Library** - Pre-built campaign templates
- [ ] **API Server** - RESTful API for integrations

---

<div align="center">

**[⬆ back to top](#adobe-genai-creative-automation-platform)**

Made with ❤️ by the Adobe GenAI Team

</div>
# adobe-genai-project
# adobe-genai-project
