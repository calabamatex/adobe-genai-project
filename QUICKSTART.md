# Quick Start Guide

## 🚀 Get Running in 5 Minutes

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Configure API Keys
```bash
cp .env.example .env
# Edit .env and add your API keys:
# - FIREFLY_API_KEY
# - FIREFLY_CLIENT_ID
# - CLAUDE_API_KEY
```

### Step 3: Validate Setup
```bash
python -m src.cli validate-config
```

### Step 4: Run Example Campaign
```bash
python -m src.cli process --brief examples/campaign_brief.json --verbose
```

## 📊 What to Expect

The pipeline will:
1. Load campaign brief with 2 products
2. Parse brand guidelines (colors, fonts, style)
3. Parse localization rules (3 locales: en-US, es-MX, fr-CA)
4. Generate hero images using Firefly API
5. Create 3 aspect ratios per product per locale
6. Apply text overlays with brand compliance
7. Save 18 total assets (2 products × 3 locales × 3 ratios)

**Expected Output:**
```
output/
└── SUMMER2026/
    ├── en-US/
    │   ├── HEADPHONES-001/
    │   │   ├── 1x1/HEADPHONES-001_1x1_en-US.png
    │   │   ├── 9x16/HEADPHONES-001_9x16_en-US.png
    │   │   └── 16x9/HEADPHONES-001_16x9_en-US.png
    │   └── SMARTWATCH-002/
    ├── es-MX/
    └── fr-CA/
    └── campaign_report.json
```

## 🎥 For Demo/Presentation

1. **Show Configuration:**
   ```bash
   python -m src.cli validate-config
   ```

2. **Show Examples:**
   ```bash
   python -m src.cli list-examples
   ```

3. **Run Campaign (Verbose):**
   ```bash
   python -m src.cli process --brief examples/campaign_brief.json --verbose
   ```

4. **Show Results:**
   - Navigate to `output/SUMMER2026/`
   - Show generated images
   - Open `campaign_report.json`

## 🧪 Run Tests

```bash
# Run all tests
pytest

# With coverage
pytest --cov=src --cov-report=html

# Open coverage report
open htmlcov/index.html
```

## 📝 Key Files to Review

- **README.md** - Complete documentation
- **src/pipeline.py** - Main orchestrator logic
- **src/genai/claude.py** - AI extraction & localization
- **src/genai/firefly.py** - Image generation
- **examples/campaign_brief.json** - Example input
- **examples/guidelines/** - Brand & localization rules

## ⏱️ Performance Target

- **Target:** <3 minutes for 2-product, 2-locale campaign
- **Typical:** 2-2.5 minutes
- **Output:** 18 high-quality campaign assets

## 🎯 Next Steps

1. Add your real API keys to `.env`
2. Run the example campaign
3. Review generated assets
4. Customize `campaign_brief.json` for your use case
5. Add your own brand guidelines
6. Scale to more products/locales

## 💡 Tips

- Start with `--dry-run` to validate without processing
- Use `--verbose` to see detailed progress
- Check `campaign_report.json` for complete metrics
- Each run creates timestamped output directory
- Reuses hero images across locales for efficiency

---

**Need Help?** Check README.md for troubleshooting and detailed documentation.
