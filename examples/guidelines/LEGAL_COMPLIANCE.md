# Legal Compliance Guidelines

Comprehensive legal compliance checking for campaign content to ensure regulatory adherence and reduce legal risk.

## Overview

The legal compliance system validates campaign content against industry-specific regulations, including:

- **FTC** (Federal Trade Commission) - Truth in Advertising
- **FDA** (Food and Drug Administration) - Health claims
- **SEC/FINRA** - Financial services
- **COPPA** - Children's privacy
- **CAN-SPAM** - Email marketing
- **Industry-specific regulations**

## Quick Start

### 1. Choose Legal Guidelines

Select or create guidelines for your industry:

```yaml
# examples/guidelines/legal_compliance_general.yaml
prohibited_words:
  - "guarantee"
  - "free"
  - "cure"

prohibited_claims:
  - "guaranteed results"
  - "100% effective"

require_substantiation: true
```

### 2. Reference in Campaign

```json
{
  "campaign_id": "MY_CAMPAIGN",
  "legal_compliance_file": "examples/guidelines/legal_compliance_general.yaml",
  ...
}
```

### 3. Run Campaign

```bash
./run_cli.sh examples/my_campaign.json
```

The system will automatically check all content and report violations.

## Available Guidelines

| File | Industry | Description |
|------|----------|-------------|
| `legal_compliance_general.yaml` | General | Standard consumer products/services |
| `legal_compliance_health.yaml` | Health/Wellness | Supplements, fitness, wellness (FDA/FTC) |
| `legal_compliance_financial.yaml` | Financial | Banking, investment, insurance (SEC/FINRA) |

## What Gets Checked

### Campaign Content
- ✅ Headlines
- ✅ Subheadlines
- ✅ Call-to-action (CTA) text
- ✅ Product descriptions
- ✅ Product features
- ✅ Marketing claims

### Validation Types
1. **Prohibited Words** - Terms that cannot be used
2. **Prohibited Phrases** - Complete phrases that are banned
3. **Prohibited Claims** - Unsubstantiated marketing claims
4. **Restricted Terms** - Words requiring context/disclaimers
5. **Protected Trademarks** - Competitor trademarks
6. **Superlatives** - "Best", "perfect" (may require proof)
7. **Age Restrictions** - Minimum age requirements
8. **Geographic Restrictions** - Region-specific prohibitions
9. **Required Disclaimers** - Mandatory disclosure text

## Violation Severities

### 🚨 ERROR (Must Fix)
- **Prohibited words** found in content
- **Prohibited phrases** detected
- **Prohibited claims** made without substantiation
- **Protected trademarks** used
- **Locale-specific violations**

Campaign generation will be **blocked** until errors are fixed.

### ⚠️ WARNING (Review Recommended)
- **Restricted terms** used in questionable context
- **Superlatives** that may require substantiation
- **Claims** that need verification
- **Testimonial** language without disclaimers

Campaign can proceed but review is recommended.

### ℹ️ INFO (For Your Information)
- **Required disclaimers** that should be included
- **Industry regulations** to follow
- **Best practices** reminders
- **Substantiation** requirements

## Configuration Options

### Prohibited Words
Words that cannot appear in any context:

```yaml
prohibited_words:
  - "guarantee"
  - "cure"
  - "FDA-approved"  # Unless actually approved
  - "free"          # Often requires disclaimer
```

### Prohibited Phrases
Complete phrases that are banned:

```yaml
prohibited_phrases:
  - "guaranteed results"
  - "100% effective"
  - "risk-free"
  - "no side effects"
```

### Prohibited Claims
Marketing claims without substantiation:

```yaml
prohibited_claims:
  - "scientifically proven"  # Without studies
  - "doctor recommended"     # Without endorsements
  - "best in class"          # Without comparative data
```

### Restricted Terms
Terms requiring specific context:

```yaml
restricted_terms:
  "natural":
    - "100%"        # Needs substantiation
    - "completely"  # Needs substantiation
  "organic":
    - "certified"   # Requires certification proof
```

### Age Restrictions

```yaml
age_restrictions: 18  # Minimum age (e.g., alcohol, supplements)
```

### Restricted Audiences

```yaml
restricted_audiences:
  - "children under 13"  # COPPA compliance
  - "minors"
  - "pregnant women"     # For certain products
```

### Geographic Restrictions

```yaml
restricted_regions:
  - "California"  # State-specific restrictions
  - "EU"          # GDPR considerations
```

### Industry Regulations

```yaml
industry_regulations:
  - "FTC"    # Truth in Advertising
  - "FDA"    # Health claims
  - "SEC"    # Financial services
  - "COPPA"  # Children's privacy
```

### Protected Trademarks

```yaml
protected_trademarks:
  - "Competitor Brand A"
  - "Competitor Brand B"
```

### Content Standards

```yaml
require_substantiation: true   # Claims must be substantiated
prohibit_superlatives: false   # Allow "best", "perfect" with proof
```

### Required Disclaimers

```yaml
required_disclaimers:
  general: "Results may vary. Individual results not guaranteed."
  health: "This product is not intended to diagnose, treat, cure, or prevent any disease."
  financial: "Past performance does not guarantee future results."
```

### Locale-Specific Rules

```yaml
locale_restrictions:
  "en-US":
    prohibited_words:
      - "free"  # Requires context in US
    require_disclaimers: true

  "en-GB":
    prohibited_words:
      - "bespoke"  # Overused in UK
    require_disclaimers: true
```

## Industry-Specific Guidelines

### General Consumer Products

**Use:** `legal_compliance_general.yaml`

**Covers:**
- FTC Truth in Advertising
- CAN-SPAM email regulations
- TCPA phone marketing
- General consumer protection

**Key Restrictions:**
- No unsubstantiated claims
- "Free" requires context
- Testimonials need disclaimers
- Superlatives need proof

### Health & Wellness

**Use:** `legal_compliance_health.yaml`

**Covers:**
- FDA regulations
- DSHEA (Dietary Supplement Act)
- FTC health claims
- cGMP manufacturing

**Key Restrictions:**
- Cannot claim to "cure", "treat", or "prevent" disease
- Must include FDA disclaimer
- Requires medical consultation disclaimer
- Age restrictions (18+)
- Very strict on superlatives

### Financial Services

**Use:** `legal_compliance_financial.yaml`

**Covers:**
- SEC regulations
- FINRA rules
- CFPB consumer protection
- Truth in Lending (Reg Z)
- Truth in Savings (Reg DD)

**Key Restrictions:**
- No "guaranteed returns"
- No "risk-free investment"
- Past performance disclaimers required
- APR disclosures required
- Age restrictions (18+)

## Example Violations & Fixes

### Example 1: Health Product

**❌ Violation:**
```yaml
headline: "Cure Your Back Pain Forever"
```

**Error:** Prohibited word "cure" found

**✅ Fix:**
```yaml
headline: "Support Back Health and Comfort"
```

### Example 2: Financial Service

**❌ Violation:**
```yaml
headline: "Guaranteed 10% Returns"
```

**Error:** Prohibited phrase "guaranteed returns"

**✅ Fix:**
```yaml
headline: "Competitive Returns on Your Investment"
disclaimer: "Past performance does not guarantee future results."
```

### Example 3: General Product

**❌ Violation:**
```yaml
headline: "100% Free Product Trial"
```

**Warning:** "Free" requires disclaimer

**✅ Fix:**
```yaml
headline: "Try Risk-Free for 30 Days"
disclaimer: "Shipping and handling charges may apply."
```

### Example 4: Superlative

**❌ Violation:**
```yaml
headline: "The Best Product Ever Made"
```

**Warning:** Superlative "best" requires substantiation

**✅ Fix:**
```yaml
headline: "Award-Winning Design Excellence"
# With documented award
```

## Compliance Report Example

When violations are found:

```
⚠️  Legal Compliance Report
==================================================

🚨 ERRORS (2) - Must be fixed:
--------------------------------------------------
  • [headline] Prohibited word 'guarantee' found in headline
    💡 Remove or replace 'guarantee'

  • [product_description] Prohibited claim 'clinically proven' found in product_description
    💡 Remove unsubstantiated claim

⚠️  WARNINGS (1) - Review recommended:
  • [headline] Superlative 'best' may require substantiation
    💡 Replace 'best' with verifiable claim or add substantiation

ℹ️  INFO (1) - For your information:
  • [campaign] Required disclaimer for category 'general': Results may vary
    💡 Ensure disclaimer is included in final materials

==================================================
Total: 2 errors, 1 warnings, 1 info
```

## Creating Custom Guidelines

### Step 1: Start with Template

```bash
cp examples/guidelines/legal_compliance_general.yaml \
   examples/guidelines/legal_compliance_custom.yaml
```

### Step 2: Customize for Your Needs

```yaml
source_file: "examples/guidelines/legal_compliance_custom.yaml"

prohibited_words:
  - "your_prohibited_word"
  - "another_term"

prohibited_claims:
  - "your specific claim to avoid"

industry_regulations:
  - "Your Industry Regulator"
```

### Step 3: Test

```bash
./run_cli.sh examples/test_campaign.json
```

## Best Practices

### 1. Choose the Right Guidelines
- **General products**: Use `legal_compliance_general.yaml`
- **Health/wellness**: Use `legal_compliance_health.yaml`
- **Financial**: Use `legal_compliance_financial.yaml`
- **Custom**: Create industry-specific guidelines

### 2. Fix Errors Before Launch
- All **ERROR** level violations must be resolved
- Review all **WARNING** level violations
- Note **INFO** level reminders

### 3. Include Disclaimers
- Add required disclaimers to final materials
- Ensure disclaimers are visible and clear
- Include all legally required disclosures

### 4. Document Substantiation
- Keep evidence for all claims made
- Document comparative claims
- Maintain testimonial permissions

### 5. Review with Legal Team
- Have legal counsel review final content
- Get approval for industry-specific claims
- Verify compliance with local regulations

## Locale-Specific Compliance

Different markets have different legal requirements:

### United States (en-US)
- FTC Truth in Advertising
- FDA regulations (health products)
- State-specific laws (California Prop 65, etc.)

### United Kingdom (en-GB)
- ASA (Advertising Standards Authority)
- FCA (Financial Conduct Authority)
- MHRA (Medicines and Healthcare products)

### Canada (en-CA)
- Competition Bureau
- Health Canada
- Provincial regulations

### European Union
- GDPR data protection
- EU consumer protection directives
- Country-specific advertising laws

## Integration with Pipeline

The legal checker integrates automatically:

1. **Pre-Generation Check**: Content validated before image generation
2. **Error Blocking**: Errors block campaign generation
3. **Warning Display**: Warnings shown but don't block
4. **Report Generation**: Detailed compliance report created

## Troubleshooting

### Campaign Blocked by Legal Check

**Solution:**
1. Review compliance report
2. Fix all ERROR level violations
3. Rerun campaign

### False Positives

**Solution:**
1. Review the specific violation
2. If legitimate use, consider:
   - Rewording to avoid flagged term
   - Adding to `restricted_terms` instead of `prohibited_words`
   - Creating custom guidelines

### Industry Not Covered

**Solution:**
1. Start with `legal_compliance_general.yaml`
2. Add industry-specific restrictions
3. Consult legal counsel for requirements
4. Create custom guidelines file

## Legal Disclaimer

**Important:** This compliance checking system is a tool to help identify potential legal issues. It does NOT replace legal counsel. Always consult with qualified legal professionals before launching campaigns, especially for regulated industries.

The system checks for common compliance issues but may not catch all legal problems. Final legal review by qualified counsel is strongly recommended.

## Related Documentation

- **Brand Guidelines**: `examples/guidelines/README.md`
- **Text Customization**: `docs/TEXT_CUSTOMIZATION.md`
- **Logo Placement**: `docs/LOGO_PLACEMENT.md`

## Support

For issues or questions about legal compliance checking:
- Review this documentation
- Check example guidelines files
- Consult your legal team
- Review industry-specific regulations
