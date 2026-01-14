# Legal Compliance Examples - Violations vs Compliant Alternatives

This document shows real-world examples of legal violations and their compliant alternatives for health products.

## Test Results Summary

| Test | Errors | Warnings | Info | Result |
|------|--------|----------|------|--------|
| **Non-Compliant** | 16 | 0 | 5 | ❌ **BLOCKED** |
| **Compliant** | 0 | 1 | 5 | ✅ **PASSED** |

---

## Headline Examples

### ❌ NON-COMPLIANT
```
"Guaranteed Results - Cure Your Health Problems!"
```

**Violations:**
- ❌ "Guaranteed" - Prohibited word
- ❌ "Cure" - Prohibited word (health products cannot claim to cure)

### ✅ COMPLIANT
```
"Support Your Wellness Journey"
```

**Why it works:**
- Uses supportive language ("support") instead of medical claims
- No guarantees or prohibited medical terms

---

## Subheadline Examples

### ❌ NON-COMPLIANT
```
"100% effective miracle solution with no side effects"
```

**Violations:**
- ❌ "100% effective" - Prohibited phrase (unsubstantiated claim)
- ❌ "miracle" - Prohibited word
- ❌ "no side effects" - Prohibited phrase (can't guarantee)

### ✅ COMPLIANT
```
"Natural supplement designed to promote healthy living"
```

**Why it works:**
- Uses "natural" (allowed with substantiation)
- "Promote healthy living" is acceptable with disclaimers
- No absolute claims or guarantees

---

## Call-to-Action (CTA) Examples

### ❌ NON-COMPLIANT
```
"Get Free Trial - FDA-approved treatment"
```

**Violations:**
- ❌ "Free" - Requires disclaimer about shipping/handling
- ❌ "FDA-approved" - Cannot claim unless actually approved
- ❌ "treatment" - Medical term requiring FDA approval

### ✅ COMPLIANT
```
"Try Risk-Free for 30 Days"
```

**Why it works:**
- "Risk-Free" with return policy is acceptable
- Specific timeframe (30 days) is factual
- No medical or FDA claims

---

## Product Description Examples

### ❌ NON-COMPLIANT
```
"Our scientifically proven formula will cure diseases and prevent illness.
Doctor recommended with guaranteed weight loss of 20 pounds in 10 days."
```

**Violations:**
- ❌ "scientifically proven" - Requires peer-reviewed studies
- ❌ "cure diseases" - Medical claim, prohibited
- ❌ "prevent illness" - Medical claim, prohibited
- ❌ "Doctor recommended" - Requires actual endorsements
- ❌ "guaranteed weight loss" - Cannot guarantee results
- ❌ "20 pounds in 10 days" - Unrealistic/unsafe claim

### ✅ COMPLIANT
```
"A carefully formulated blend of natural ingredients designed to support
overall wellness. Our product follows strict quality standards and is
manufactured in a certified facility."
```

**Why it works:**
- "Formulated" and "designed to support" are acceptable
- Focuses on quality and manufacturing standards
- No medical claims or guarantees
- No specific weight loss or health outcome promises

---

## Product Features Examples

### ❌ NON-COMPLIANT

**Feature 1:**
```
"Clinically proven to treat medical conditions"
```
- ❌ "Clinically proven to treat" - Medical claim
- ❌ "treat medical conditions" - Requires FDA approval

**Feature 2:**
```
"FDA-approved pharmaceutical-grade medicine"
```
- ❌ "FDA-approved" - Cannot claim unless true
- ❌ "pharmaceutical" - Drug terminology
- ❌ "medicine" - Drug terminology

**Feature 3:**
```
"100% safe with no side effects"
```
- ❌ "100% safe" - Cannot guarantee absolute safety
- ❌ "no side effects" - Cannot guarantee

**Feature 4:**
```
"Guaranteed to reverse aging"
```
- ❌ "Guaranteed" - Cannot guarantee results
- ❌ "reverse aging" - Unsubstantiated anti-aging claim

### ✅ COMPLIANT

**Feature 1:**
```
"Contains essential vitamins and minerals"
```
- ✅ Factual statement about ingredients

**Feature 2:**
```
"Made with natural ingredients"
```
- ✅ Acceptable with substantiation

**Feature 3:**
```
"Third-party tested for quality"
```
- ✅ Verifiable quality claim

**Feature 4:**
```
"Supports healthy lifestyle habits"
```
- ✅ Supportive language, not medical claim

---

## Required Disclaimers (Always Include)

For health products, the following disclaimers are **required**:

### 1. Product Disclaimer
```
"This product is not intended to diagnose, treat, cure, or prevent any disease."
```

### 2. Results Disclaimer
```
"Results may vary. Individual results are not guaranteed."
```

### 3. Medical Consultation Disclaimer
```
"Consult your physician before starting any supplement regimen."
```

### 4. FDA Disclaimer
```
"These statements have not been evaluated by the Food and Drug Administration."
```

### 5. Diet/Exercise Disclaimer
```
"As part of a balanced diet and exercise program."
```

---

## Word Substitution Guide

| ❌ Avoid | ✅ Use Instead |
|---------|---------------|
| Cure | Support, Maintain, Promote |
| Treat | Help, Assist, Support |
| Prevent | Support, Maintain |
| Guarantee | May help, Designed to |
| Miracle | Effective, Beneficial |
| FDA-approved | Quality tested, Certified facility |
| Clinically proven | Research-backed (with studies) |
| Doctor recommended | Professionally formulated |
| 100% effective | Effective for many users |
| No side effects | Generally well-tolerated |
| Lose X pounds in Y days | Support healthy weight management |
| Reverse aging | Support healthy aging |

---

## Severity Levels Explained

### 🚨 ERROR (Blocks Campaign)
- Prohibited words found (cure, treat, prevent, guarantee)
- Prohibited phrases detected (100% effective, no side effects)
- Unsubstantiated medical claims
- Misuse of FDA terminology

**Action:** Campaign generation is **BLOCKED** until all errors are fixed.

### ⚠️ WARNING (Review Recommended)
- Restricted terms used in questionable context
- Superlatives without substantiation
- Claims needing verification
- Testimonial language without disclaimers

**Action:** Campaign can proceed, but **review is strongly recommended**.

### ℹ️ INFO (Informational)
- Required disclaimers that should be included
- Industry regulations to follow
- Best practices reminders
- Substantiation requirements

**Action:** For your information only. Campaign proceeds normally.

---

## Industry-Specific Guidelines

### Health & Wellness
**File:** `legal_compliance_health.yaml`

**Most Strict:**
- Cannot use: cure, treat, prevent, diagnose
- Requires FDA disclaimer
- Age restriction: 18+
- Requires medical consultation disclaimer

### Financial Services
**File:** `legal_compliance_financial.yaml`

**Key Restrictions:**
- No "guaranteed returns"
- No "risk-free investment"
- Requires past performance disclaimer
- Age restriction: 18+

### General Consumer Products
**File:** `legal_compliance_general.yaml`

**Standard Protections:**
- FTC Truth in Advertising
- Substantiation required for claims
- Testimonials need disclaimers
- "Free" requires context

---

## Quick Testing

### Test Non-Compliant Campaign
```bash
./run_cli.sh examples/campaigns/test_legal_compliance.json
```

**Expected Result:** ❌ Blocked with 16 errors

### Test Compliant Campaign
```bash
./run_cli.sh examples/campaigns/test_legal_compliance_compliant.json
```

**Expected Result:** ✅ Passes with 0 errors, 1 warning

---

## Best Practices

1. **Choose the Right Guidelines**
   - Health products → `legal_compliance_health.yaml`
   - Financial services → `legal_compliance_financial.yaml`
   - General products → `legal_compliance_general.yaml`

2. **Fix ALL Errors**
   - Campaign will not proceed with ERROR-level violations
   - Review compliance report carefully
   - Use word substitution guide

3. **Review Warnings**
   - Warnings don't block but should be reviewed
   - Consider adding disclaimers
   - Verify claims can be substantiated

4. **Include Disclaimers**
   - Add all required disclaimers to final materials
   - Make them clearly visible
   - Include in all marketing materials

5. **Consult Legal Counsel**
   - This tool aids compliance but doesn't replace legal review
   - Always have final content reviewed by legal team
   - Keep documentation of claim substantiation

---

## Related Documentation

- **Full Guide:** `examples/guidelines/LEGAL_COMPLIANCE.md`
- **Health Guidelines:** `examples/guidelines/legal_compliance_health.yaml`
- **Financial Guidelines:** `examples/guidelines/legal_compliance_financial.yaml`
- **General Guidelines:** `examples/guidelines/legal_compliance_general.yaml`
