# Campaign Generator

Easily create new campaign brief files from templates.

## Quick Start

### Option 1: Using the Helper Script

```bash
./create_campaign.sh \
  --campaign-id "HOLIDAY2026" \
  --campaign-name "Holiday Tech Sale 2026" \
  --brand-name "TechStyle" \
  --headline "Holiday Tech Savings" \
  --subheadline "Save Big on Premium Electronics" \
  --cta "Shop Holiday Deals"
```

### Option 2: Using the CLI Directly

```bash
python -m src.cli new-campaign \
  --campaign-id "SPRING2027" \
  --campaign-name "Spring Collection 2027" \
  --brand-name "YourBrand"
```

### Option 3: Interactive Mode

```bash
./create_campaign.sh \
  --campaign-id "SUMMER2027" \
  --campaign-name "Summer Campaign" \
  --interactive
```

Interactive mode will prompt you for each value.

## Command Options

| Option | Required | Description | Example |
|--------|----------|-------------|---------|
| `--campaign-id` | ✅ Yes | Unique identifier | `FALL2026` |
| `--campaign-name` | ✅ Yes | Human-readable name | `"Fall Collection"` |
| `--brand-name` | No | Brand name | `"TechStyle"` |
| `--headline` | No | Main headline | `"Discover Innovation"` |
| `--subheadline` | No | Subheadline | `"Premium Quality"` |
| `--cta` | No | Call to action | `"Shop Now"` |
| `-o, --output` | No | Custom output path | `campaigns/my_campaign.json` |
| `-i, --interactive` | No | Interactive mode | (flag) |

## Generated File Structure

The generator creates a JSON file at `examples/{campaign_id}_campaign.json` with:

```json
{
  "campaign_id": "YOUR_ID",
  "campaign_name": "Your Name",
  "brand_name": "Your Brand",
  "campaign_message": {
    "headline": "Your Headline",
    "subheadline": "Your Subheadline",
    "cta": "Your CTA"
  },
  "products": [
    {
      "product_id": "PRODUCT-001",
      "product_name": "Premium Product",
      ...
    }
  ],
  "aspect_ratios": ["1:1", "9:16", "16:9"],
  "image_generation_backend": "openai",
  "target_locales": ["en-US"]
}
```

## Next Steps After Generation

1. **Edit the generated file** to add your specific products:
   ```bash
   vi examples/fall2026_campaign.json
   ```

2. **Run the campaign**:
   ```bash
   ./run_cli.sh examples/fall2026_campaign.json
   ```
   Or:
   ```bash
   python -m src.cli process --brief examples/fall2026_campaign.json
   ```

## Custom Templates

Create your own templates in `examples/templates/`:

```json
{
  "campaign_id": "{{CAMPAIGN_ID}}",
  "custom_field": "{{MY_CUSTOM_FIELD}}",
  ...
}
```

Use custom template:
```bash
python -m src.cli new-campaign \
  --campaign-id "TEST" \
  --campaign-name "Test" \
  --template examples/templates/my_template.json
```

## Examples

### Minimal Campaign
```bash
./create_campaign.sh \
  --campaign-id "TEST2026" \
  --campaign-name "Test Campaign"
```

### Full Campaign with All Options
```bash
./create_campaign.sh \
  --campaign-id "COMPLETE2026" \
  --campaign-name "Complete Campaign Example" \
  --brand-name "TechCorp" \
  --headline "Revolutionary Technology" \
  --subheadline "Experience the Future Today" \
  --cta "Discover Now" \
  --output campaigns/complete_example.json
```

### Multi-Locale Campaign
After generating, edit the JSON to add locales:
```json
{
  "enable_localization": true,
  "target_locales": ["en-US", "es-MX", "fr-CA"],
  "localization_guidelines_file": "examples/guidelines/localization_rules.yaml"
}
```

## Tips

- **Campaign IDs** should be unique (e.g., `FALL2026`, `HOLIDAY2026`)
- **File naming** is automatic: `FALL2026` → `examples/fall2026_campaign.json`
- **Edit after generation** - The template creates a starting point
- **Reuse campaigns** - Edit the campaign_id to create variations

## Troubleshooting

**Q: Generated file has default values**
A: Pass values via command line options or use `--interactive` mode

**Q: Want to customize products**
A: Edit the generated JSON file manually to add your specific products

**Q: Need different aspect ratios**
A: Edit the `aspect_ratios` array in the generated file

**Q: Want to use existing assets**
A: Add `existing_assets` to products in the generated file
