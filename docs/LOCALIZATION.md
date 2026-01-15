# Localization System

> **Comprehensive guide to AI-powered localization, cultural adaptation, and multi-market campaign generation**

## Overview

The Localization System uses **Claude 3.5 Sonnet** to provide intelligent, culturally-aware message adaptation across 20+ locales. Unlike simple translation, it preserves brand voice, adapts cultural references, and ensures messaging resonates with local audiences.

---

## Table of Contents

- [Quick Start](#quick-start)
- [How It Works](#how-it-works)
- [Supported Locales](#supported-locales)
- [Cultural Adaptation](#cultural-adaptation)
- [Configuration](#configuration)
- [Localization Guidelines](#localization-guidelines)
- [Examples by Market](#examples-by-market)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

---

## Quick Start

### 1. Enable Localization

In your campaign brief:

```json
{
  "campaign_id": "GLOBAL2026",
  "enable_localization": true,
  "target_locales": ["en-US", "es-MX", "fr-FR", "de-DE", "ja-JP"],
  "localization_guidelines_file": "examples/guidelines/localization_rules.yaml",
  ...
}
```

### 2. Create Localization Guidelines (Optional)

`localization_rules.yaml`:

```yaml
# Tone and Voice
brand_voice: "friendly"              # Tone across all locales
formality_level: "casual"            # Casual, professional, formal

# Market-Specific Rules
locale_rules:
  "es-MX":
    formality: "casual"
    use_local_idioms: true
    avoid_spain_spanish: true

  "ja-JP":
    formality: "polite"
    use_honorifics: true
    prefer_hiragana: false

# Cultural Considerations
avoid_cultural_references:
  - "Black Friday"                   # Not global
  - "Thanksgiving"                   # US-specific

preserve_elements:
  - brand_name
  - product_names
  - technical_terms
```

### 3. Run Campaign

```bash
./run_cli.sh campaign.json
```

**Result:** Culturally-adapted assets for each locale!

---

## How It Works

### AI-Powered Localization Process

```
Original Message (en-US)
    ↓
Claude 3.5 Sonnet Analysis
    ↓
Cultural Context Understanding
    ↓
Tone and Voice Preservation
    ↓
Local Idiom Adaptation
    ↓
Culturally-Adapted Message
    ↓
Applied to Marketing Asset
```

### What Makes It Different

**Traditional Translation:**
- Word-for-word conversion
- Literal meaning preserved
- Cultural context lost
- Tone often changes

**AI-Powered Localization:**
- ✅ Cultural adaptation
- ✅ Tone preservation
- ✅ Local idiom usage
- ✅ Brand voice maintained
- ✅ Context awareness
- ✅ Market-specific phrasing

### Example Comparison

**Original (en-US):**
```
"Score big savings this weekend!"
```

**Traditional Translation (es-MX):**
```
"Anote grandes ahorros este fin de semana"
(Literal, sounds awkward)
```

**AI-Powered Localization (es-MX):**
```
"¡Aprovecha descuentos increíbles este fin de semana!"
(Natural, culturally appropriate)
```

---

## Supported Locales

### Fully Supported (20+ locales)

#### North America

| Locale | Market | Population | Notes |
|--------|--------|------------|-------|
| **en-US** | United States | 330M | Default, American English |
| **en-CA** | Canada | 30M | Canadian English spelling |
| **fr-CA** | Canada | 8M | Québécois French |
| **es-MX** | Mexico | 130M | Mexican Spanish |

#### Europe

| Locale | Market | Population | Notes |
|--------|--------|------------|-------|
| **en-GB** | United Kingdom | 67M | British English spelling |
| **fr-FR** | France | 65M | European French |
| **de-DE** | Germany | 83M | High German |
| **es-ES** | Spain | 47M | Castilian Spanish |
| **it-IT** | Italy | 60M | Standard Italian |
| **nl-NL** | Netherlands | 17M | Dutch |
| **pt-PT** | Portugal | 10M | European Portuguese |
| **sv-SE** | Sweden | 10M | Swedish |
| **pl-PL** | Poland | 38M | Polish |
| **tr-TR** | Turkey | 84M | Turkish |

#### Asia Pacific

| Locale | Market | Population | Notes |
|--------|--------|------------|-------|
| **ja-JP** | Japan | 126M | Japanese (Kanji/Hiragana/Katakana) |
| **zh-CN** | China | 1.4B | Simplified Chinese |
| **zh-TW** | Taiwan | 24M | Traditional Chinese |
| **ko-KR** | South Korea | 52M | Korean (Hangul) |
| **th-TH** | Thailand | 70M | Thai |

#### Latin America

| Locale | Market | Population | Notes |
|--------|--------|------------|-------|
| **pt-BR** | Brazil | 213M | Brazilian Portuguese |
| **es-AR** | Argentina | 45M | Argentine Spanish |
| **es-CL** | Chile | 19M | Chilean Spanish |

### Experimental Support

- **ar-SA** - Arabic (Saudi Arabia)
- **he-IL** - Hebrew (Israel)
- **vi-VN** - Vietnamese
- **id-ID** - Indonesian
- **ms-MY** - Malay (Malaysia)

---

## Cultural Adaptation

### Tone and Voice Preservation

#### Brand Voice Options

**Friendly:**
```yaml
brand_voice: "friendly"
```
- Warm, approachable
- Conversational language
- Personal pronouns ("you", "we")

**Example:**
- en-US: "We've got something special for you!"
- es-MX: "¡Tenemos algo especial para ti!"
- fr-FR: "On a quelque chose de spécial pour toi !"

**Professional:**
```yaml
brand_voice: "professional"
```
- Business-appropriate
- Formal but accessible
- Industry terminology

**Example:**
- en-US: "Enhance your workflow efficiency"
- de-DE: "Optimieren Sie Ihre Arbeitsabläufe"
- ja-JP: "業務効率を向上させます"

**Playful:**
```yaml
brand_voice: "playful"
```
- Fun, energetic
- Casual language
- Emoji-friendly (where appropriate)

**Example:**
- en-US: "Get ready to level up! 🚀"
- es-MX: "¡Prepárate para subir de nivel! 🚀"
- pt-BR: "Prepare-se para evoluir! 🚀"

### Formality Levels

#### Casual (tu/du/você)
```yaml
formality_level: "casual"
```

**Uses informal pronouns:**
- Spanish: "tú"
- French: "tu"
- German: "du"
- Portuguese: "você"

**Best For:** Young audiences, lifestyle brands, social media

#### Professional (usted/vous/Sie)
```yaml
formality_level: "professional"
```

**Uses formal pronouns:**
- Spanish: "usted"
- French: "vous"
- German: "Sie"

**Best For:** B2B, professional services, finance

#### Formal
```yaml
formality_level: "formal"
```

**Highest level of respect:**
- Japanese: Keigo (敬語) with honorifics
- Korean: Formal speech levels
- Chinese: Honorific titles

**Best For:** Luxury brands, elder audiences, traditional markets

### Regional Variations

#### Spanish Variations

**Mexican Spanish (es-MX):**
```
- "computadora" (computer)
- "carro" (car)
- "celular" (mobile phone)
- Casual, friendly tone
```

**Spain Spanish (es-ES):**
```
- "ordenador" (computer)
- "coche" (car)
- "móvil" (mobile phone)
- More formal "vosotros" form
```

**Argentine Spanish (es-AR):**
```
- "vos" instead of "tú"
- "che" interjection
- Unique slang and expressions
```

#### Portuguese Variations

**Brazilian Portuguese (pt-BR):**
```
- "você" (you)
- "trem" (train)
- Gerund usage common
```

**European Portuguese (pt-PT):**
```
- "tu" (you, informal)
- "comboio" (train)
- Infinitive preferred over gerund
```

#### French Variations

**France French (fr-FR):**
```
- Standard French
- "tu/vous" distinction clear
```

**Canadian French (fr-CA):**
```
- Québécois expressions
- English loanwords accepted
- "magasiner" vs "faire du shopping"
```

#### English Variations

**American English (en-US):**
```
- "color", "center", "analyze"
- $ symbol before number: $99
- MM/DD/YYYY date format
```

**British English (en-GB):**
```
- "colour", "centre", "analyse"
- £ symbol before number: £99
- DD/MM/YYYY date format
```

---

## Configuration

### Localization Guidelines File

Create `localization_rules.yaml`:

```yaml
# Source Configuration
source_file: "localization_rules.yaml"

# Global Settings
brand_voice: "friendly"              # friendly, professional, playful
formality_level: "casual"            # casual, professional, formal
preserve_brand_name: true            # Keep brand name unchanged
preserve_product_names: true         # Keep product names unchanged

# Cultural Adaptations
adapt_idioms: true                   # Convert idioms to local equivalents
adapt_cultural_references: true      # Adapt cultural references
use_local_currencies: true           # Convert to local currency
use_local_date_formats: true         # Use local date formatting
use_local_units: true                # Metric vs Imperial

# Elements to Preserve
preserve_elements:
  - brand_name
  - product_names
  - model_numbers
  - technical_specifications
  - URLs
  - email_addresses
  - phone_numbers

# Elements to Avoid
avoid_cultural_references:
  - "Black Friday"                   # US-specific
  - "Super Bowl"                     # US sports
  - "Thanksgiving"                   # US holiday
  - "Halloween"                      # Limited global appeal

# Locale-Specific Rules
locale_rules:
  "en-US":
    currency: "USD"
    date_format: "MM/DD/YYYY"
    units: "imperial"

  "en-GB":
    spelling: "british"              # colour, centre, analyse
    currency: "GBP"
    date_format: "DD/MM/YYYY"
    units: "metric"

  "es-MX":
    formality: "casual"
    use_local_idioms: true
    avoid_spain_spanish: true
    currency: "MXN"

  "fr-FR":
    formality: "professional"
    use_formal_vous: true
    currency: "EUR"

  "de-DE":
    formality: "professional"
    use_formal_sie: true
    compound_words: true
    currency: "EUR"

  "ja-JP":
    formality: "polite"
    use_honorifics: true
    writing_system: "mixed"          # Kanji + Hiragana + Katakana
    currency: "JPY"

  "zh-CN":
    script: "simplified"
    formality: "neutral"
    currency: "CNY"

  "pt-BR":
    variant: "brazilian"
    formality: "casual"
    currency: "BRL"

# Translation Preferences
translation_style:
  maintain_length: "flexible"        # flexible, similar, exact
  allow_creativity: true              # Creative adaptations
  prioritize_meaning: true            # Meaning over literal translation
  adapt_humor: true                   # Adapt jokes/wordplay
```

### Campaign Brief Configuration

```json
{
  "campaign_id": "GLOBAL2026",
  "campaign_name": "Global Summer Campaign",

  "enable_localization": true,
  "localization_guidelines_file": "localization_rules.yaml",

  "target_locales": [
    "en-US",
    "es-MX",
    "fr-FR",
    "de-DE",
    "ja-JP",
    "pt-BR"
  ],

  "campaign_message": {
    "locale": "en-US",
    "headline": "Summer Savings Start Now",
    "subheadline": "Don't miss out on incredible deals",
    "cta": "Shop Now"
  }
}
```

---

## Examples by Market

### Example 1: Promotional Campaign

**Original (en-US):**
```
Headline: "Summer Savings Start Now"
Subheadline: "Don't miss out on incredible deals"
CTA: "Shop Now"
```

**Localized Versions:**

**es-MX (Mexican Spanish):**
```
Headline: "Aprovecha Descuentos de Verano"
Subheadline: "No te pierdas ofertas increíbles"
CTA: "Compra Ahora"
```

**fr-FR (French):**
```
Headline: "Les Soldes d'Été Commencent"
Subheadline: "Ne manquez pas nos offres exceptionnelles"
CTA: "Découvrir"
```

**de-DE (German):**
```
Headline: "Sommerschlussverkauf Startet Jetzt"
Subheadline: "Verpassen Sie nicht unsere tollen Angebote"
CTA: "Jetzt Shoppen"
```

**ja-JP (Japanese):**
```
Headline: "夏のセール開催中"
Subheadline: "お得な商品をお見逃しなく"
CTA: "今すぐ購入"
```

**pt-BR (Brazilian Portuguese):**
```
Headline: "Promoções de Verão Começam Agora"
Subheadline: "Não perca ofertas incríveis"
CTA: "Comprar Agora"
```

### Example 2: Product Launch

**Original (en-US):**
```
Headline: "Introducing Our Latest Innovation"
Subheadline: "Experience the future today"
CTA: "Learn More"
```

**Localized Versions:**

**en-GB (British English):**
```
Headline: "Introducing Our Latest Innovation"
Subheadline: "Experience the future today"
CTA: "Learn More"
```
*Note: Minimal changes, spelling consistent*

**es-ES (Spain Spanish):**
```
Headline: "Presentamos Nuestra Última Innovación"
Subheadline: "Experimenta el futuro hoy"
CTA: "Más Información"
```

**it-IT (Italian):**
```
Headline: "Ti Presentiamo la Nostra Ultima Innovazione"
Subheadline: "Vivi il futuro oggi"
CTA: "Scopri di Più"
```

**zh-CN (Simplified Chinese):**
```
Headline: "介绍我们最新的创新产品"
Subheadline: "今天体验未来"
CTA: "了解更多"
```

### Example 3: Lifestyle Brand

**Original (en-US):**
```
Headline: "Live Your Best Life"
Subheadline: "Style that moves with you"
CTA: "Explore Collection"
```

**Localized Versions:**

**fr-CA (Canadian French):**
```
Headline: "Vis Ta Meilleure Vie"
Subheadline: "Un style qui bouge avec toi"
CTA: "Découvre la Collection"
```

**ko-KR (Korean):**
```
Headline: "최고의 삶을 살아가세요"
Subheadline: "당신과 함께하는 스타일"
CTA: "컬렉션 보기"
```

**tr-TR (Turkish):**
```
Headline: "En İyi Hayatını Yaşa"
Subheadline: "Seninle hareket eden stil"
CTA: "Koleksiyonu Keşfet"
```

---

## Best Practices

### 1. Source Message Quality

**DO:**
- Write clear, concise source messages
- Avoid complex idioms
- Use simple sentence structures
- Be culturally neutral in source

**DON'T:**
- Use US-specific references
- Rely on wordplay/puns
- Use ambiguous phrases
- Include unexplained acronyms

### 2. Cultural Sensitivity

**Research Local Markets:**
- Understand cultural taboos
- Research local holidays
- Learn local customs
- Study competitor messaging

**Color Meanings Vary:**
- Red: Luck (China) vs Danger (Western)
- White: Purity (Western) vs Mourning (East Asia)
- Yellow: Optimism (US) vs Royalty (India)

**Number Meanings:**
- 4: Unlucky in Chinese/Japanese/Korean
- 13: Unlucky in Western cultures
- 8: Lucky in Chinese culture

### 3. Length Considerations

**Language Expansion:**
- German: +35% longer than English
- French: +20% longer
- Spanish: +20% longer
- Japanese: -10% to +10%
- Chinese: -30% to -50%

**Design Implications:**
```yaml
# Allow flexible text sizing
allow_text_wrapping: true
adjust_font_size: true
maintain_readability: true
```

### 4. Testing Localized Content

**Review Checklist:**
- [ ] Tone matches brand voice
- [ ] Cultural references appropriate
- [ ] No offensive content
- [ ] Formality level correct
- [ ] Grammar/spelling correct
- [ ] Length fits design
- [ ] CTA clear and actionable

**Native Speaker Review:**
- Use native speakers for final review
- Test on target audience
- A/B test variations
- Monitor feedback

### 5. Consistency Across Locales

**Maintain:**
- Brand positioning
- Key messages
- Product benefits
- Visual identity

**Adapt:**
- Cultural references
- Local idioms
- Formality levels
- Call-to-action phrasing

---

## Advanced Features

### Context-Aware Localization

Claude analyzes:
- **Campaign context** - Product category, target audience
- **Brand voice** - Formal vs casual, friendly vs professional
- **Cultural nuances** - Local customs, holidays, preferences
- **Market positioning** - Luxury vs budget, traditional vs modern

### Tone Preservation

**How It Works:**
1. Analyze source message tone
2. Identify key emotional elements
3. Find equivalent expressions in target locale
4. Preserve emotional impact

**Example:**
```
Source: "Get ready to rock this summer!" (energetic, casual)
es-MX: "¡Prepárate para arrasar este verano!" (same energy)
ja-JP: "この夏を楽しみましょう！" (positive, appropriate)
```

### Idiom Adaptation

**Source Idiom Detection:**
- "Hit the ground running"
- "Think outside the box"
- "Best of both worlds"

**Localization Approach:**
1. Identify idiomatic expression
2. Find cultural equivalent
3. If none exists, express core meaning

**Example:**
```
en-US: "Hit the ground running with our new product"
es-MX: "Empieza con todo con nuestro nuevo producto"
de-DE: "Starten Sie durch mit unserem neuen Produkt"
```

---

## Troubleshooting

### Issue: Localized Text Too Long

**Problem:** German/French text overflows design

**Solutions:**
1. Allow automatic font size adjustment
2. Increase text area padding
3. Use shorter headline in source
4. Enable text wrapping

```yaml
# In brand guidelines
allow_text_wrapping: true
min_font_size: 36
```

### Issue: Formal/Informal Mismatch

**Problem:** Wrong formality level for market

**Solution:** Specify in localization guidelines

```yaml
locale_rules:
  "es-MX":
    formality: "casual"           # Use "tú"
  "de-DE":
    formality: "professional"     # Use "Sie"
```

### Issue: Cultural Reference Lost

**Problem:** English idiom doesn't translate

**Solution:** AI automatically adapts

```
en-US: "Score big this weekend"
→ Idiomatic sports reference
es-MX: "Aprovecha grandes ofertas este fin de semana"
→ Adapted to direct benefit message
```

### Issue: Brand Name Changed

**Problem:** Brand name translated incorrectly

**Solution:** Add to preserve list

```yaml
preserve_elements:
  - brand_name
  - product_names
```

### Issue: Technical Terms Translated

**Problem:** Technical specifications changed

**Solution:** Mark as preserve

```yaml
preserve_elements:
  - technical_specifications
  - model_numbers
  - SKUs
```

---

## Performance Optimization

### Caching Strategy

**Hero Image Reuse:**
- Generate hero image once
- Reuse across all locales
- Only localize text overlay

**Benefits:**
- 70-90% reduction in API calls
- Faster processing (seconds vs minutes)
- Cost savings

### Batch Localization

**Process Multiple Locales:**
```python
locales = ["en-US", "es-MX", "fr-FR", "de-DE"]
# Processed concurrently with asyncio
# ~10-15 seconds for 4 locales
```

---

## Integration with Pipeline

**Localization Pipeline:**
```
1. Load source message (en-US)
2. Load localization guidelines
3. For each target locale:
   a. Detect if localization needed
   b. Call Claude for cultural adaptation
   c. Preserve brand elements
   d. Apply to image overlay
4. Generate assets for each locale
```

**When Localization Skipped:**
- Source locale matches target locale
- `enable_localization: false`
- No localization guidelines provided

---

## Related Documentation

- **[BRAND_GUIDELINES.md](BRAND_GUIDELINES.md)** - Brand guidelines system
- **[TEXT_CUSTOMIZATION.md](TEXT_CUSTOMIZATION.md)** - Text styling
- **[API.md](API.md)** - API reference
- **[ARCHITECTURE.md](../ARCHITECTURE.md)** - System architecture

---

## Summary

The Localization System provides:

✅ **AI-powered localization** with Claude 3.5 Sonnet
✅ **20+ supported locales** with cultural adaptation
✅ **Tone preservation** across languages
✅ **Context-aware translation** for brand consistency
✅ **Idiom adaptation** for natural messaging
✅ **Formality control** for market appropriateness
✅ **Regional variations** (Mexican vs Spain Spanish, etc.)
✅ **Cultural sensitivity** with configurable rules

**Ready to create globally-resonant marketing campaigns.**
