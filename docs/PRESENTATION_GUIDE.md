# Technical Presentation Guide

This guide explains how to use the `TECHNICAL_PRESENTATION.md` file for presenting the Adobe GenAI Creative Automation Platform.

## Presentation Overview

**File:** `docs/TECHNICAL_PRESENTATION.md`
**Slides:** 60+ slides covering the entire project
**Duration:** 45-60 minutes (full presentation)
**Target Audience:** Technical teams, architects, developers

---

## Slide Deck Structure

### Section 1: Introduction (Slides 1-4)
- Title slide
- Agenda
- Project overview
- Key metrics

**Duration:** 5 minutes

### Section 2: Architecture (Slides 5-8)
- High-level architecture diagram
- System components
- Layered architecture
- Data flow

**Duration:** 8 minutes

### Section 3: Technology Stack (Slides 9-10)
- Core technologies
- Dependencies
- Development tools

**Duration:** 5 minutes

### Section 4: Core Features (Slides 11-14)
- Multi-backend integration
- AI-powered localization
- Legal compliance
- Brand guidelines

**Duration:** 10 minutes

### Section 5: Phase 1 Enhancements (Slides 15-17)
- Per-element text customization
- Text outline effects
- Post-processing pipeline

**Duration:** 8 minutes

### Section 6: Implementation Details (Slides 18-25)
- Directory structure
- Data models
- Pipeline architecture
- Backend integration

**Duration:** 10 minutes

### Section 7: Quality & Operations (Slides 26-32)
- Performance metrics
- Testing strategy
- Security & compliance
- Deployment

**Duration:** 8 minutes

### Section 8: Roadmap & Q&A (Slides 33-35)
- Future plans
- Key takeaways
- Questions

**Duration:** 6 minutes

---

## Converting to Presentation Formats

### Option 1: Marp (Markdown Presentations)

**Install Marp CLI:**
```bash
npm install -g @marp-team/marp-cli
```

**Convert to PDF:**
```bash
marp docs/TECHNICAL_PRESENTATION.md --pdf --output presentations/technical-presentation.pdf
```

**Convert to PowerPoint:**
```bash
marp docs/TECHNICAL_PRESENTATION.md --pptx --output presentations/technical-presentation.pptx
```

**Preview in browser:**
```bash
marp docs/TECHNICAL_PRESENTATION.md --preview
```

### Option 2: reveal.js (Web Presentations)

**Install reveal-md:**
```bash
npm install -g reveal-md
```

**Present in browser:**
```bash
reveal-md docs/TECHNICAL_PRESENTATION.md --theme black
```

**Export to PDF:**
```bash
reveal-md docs/TECHNICAL_PRESENTATION.md --print presentations/technical-presentation.pdf
```

### Option 3: Manual Conversion to PowerPoint/Keynote

1. Open PowerPoint or Keynote
2. Create new presentation
3. Use `---` as slide separators
4. Copy content between separators to slides
5. Add formatting and images

### Option 4: Slidev (Developer-focused)

**Install Slidev:**
```bash
npm install -g @slidev/cli
```

**Start presentation:**
```bash
slidev docs/TECHNICAL_PRESENTATION.md
```

---

## Customization Tips

### For Executive Audience

**Focus on:**
- Slides 1-4 (Overview & Metrics)
- Slide 5 (High-level architecture)
- Slides 11-14 (Core features)
- Slides 33-35 (Roadmap & takeaways)

**Duration:** 15-20 minutes

**Skip:**
- Deep technical implementation details
- Code examples
- Testing specifics

### For Developer Audience

**Focus on:**
- Slides 6-8 (Detailed architecture)
- Slides 18-25 (Implementation details)
- Slides 26-32 (Testing & deployment)
- Code examples in appendices

**Duration:** 45-60 minutes

**Add:**
- Live code walkthrough
- Interactive demo
- Q&A session

### For Sales/Marketing

**Focus on:**
- Slides 1-4 (Overview)
- Slide 11 (Multi-backend benefits)
- Slide 12 (AI localization)
- Slides 15-17 (Phase 1 visual improvements)
- Slide 35 (Business value)

**Duration:** 20-25 minutes

**Emphasize:**
- Cost savings (70-90% reduction)
- Speed improvements
- Quality enhancements
- Competitive advantages

---

## Adding Visual Assets

### Architecture Diagrams

Create diagrams using:
- **draw.io** (diagrams.net)
- **Lucidchart**
- **Mermaid** (Markdown-based)

Example locations:
```
docs/images/
├── architecture-overview.png
├── pipeline-flow.png
├── backend-integration.png
└── directory-structure.png
```

Update slides with images:
```markdown
# System Architecture

![Architecture Overview](images/architecture-overview.png)
```

### Screenshots

Add screenshots for:
- Generated campaign assets
- Brand guidelines examples
- Campaign reports
- CLI usage

### Code Syntax Highlighting

The Markdown already includes code blocks with syntax highlighting:
```python
# Example code
def generate_image(prompt: str):
    pass
```

Most presentation tools will render this properly.

---

## Presentation Tips

### Before the Presentation

1. **Test the setup**
   - Convert to desired format
   - Check all code blocks render correctly
   - Verify images display properly

2. **Prepare demo**
   - Have campaign brief ready
   - Pre-generate some assets
   - Prepare fallback screenshots

3. **Timing**
   - Practice full run-through
   - Mark key slides for emphasis
   - Plan Q&A time

### During the Presentation

1. **Introduction (5 min)**
   - Set context and goals
   - Introduce team
   - State what audience will learn

2. **Technical Deep Dive (30-40 min)**
   - Walk through architecture
   - Explain key decisions
   - Show code examples
   - Demonstrate features

3. **Live Demo (10 min)**
   - Generate campaign
   - Show Phase 1 features
   - Display outputs

4. **Q&A (10-15 min)**
   - Answer questions
   - Discuss future plans
   - Gather feedback

### Common Questions to Prepare For

**Architecture:**
- Q: Why three AI backends?
- A: Flexibility, cost optimization, quality comparison, vendor lock-in prevention

**Performance:**
- Q: How long does a campaign take?
- A: 6-18s per asset, dominated by AI generation (5-15s)

**Cost:**
- Q: How much does it cost per campaign?
- A: 70-90% reduction through hero reuse; varies by backend and volume

**Scalability:**
- Q: Can it handle 100+ products?
- A: Yes, tested up to 50; concurrent processing enables scale

**Security:**
- Q: How are API keys managed?
- A: Environment variables only, never committed, validated at startup

**Legal:**
- Q: Does it guarantee legal compliance?
- A: Provides automated checking against templates; final review recommended

---

## Exporting Formats

### PDF (Universal)

**Pros:**
- Works everywhere
- Maintains formatting
- Printable

**Cons:**
- No animations
- Static only

**Command:**
```bash
marp docs/TECHNICAL_PRESENTATION.md --pdf
```

### PowerPoint/PPTX (Corporate)

**Pros:**
- Widely used in enterprise
- Editable after export
- Animation support

**Cons:**
- May need formatting adjustments
- Platform dependent

**Command:**
```bash
marp docs/TECHNICAL_PRESENTATION.md --pptx
```

### HTML (Interactive)

**Pros:**
- Animations possible
- Interactive elements
- Code highlighting

**Cons:**
- Requires browser
- Larger file size

**Command:**
```bash
reveal-md docs/TECHNICAL_PRESENTATION.md --static presentations/html
```

---

## Creating Shorter Versions

### 15-Minute Executive Summary

**Slides to include:**
1. Title (Slide 1)
2. Agenda (Slide 2)
3. Overview (Slide 3-4)
4. Architecture diagram (Slide 5)
5. Key features (Slide 11-14)
6. Phase 1 highlights (Slide 15)
7. Business value (Slide 35)
8. Q&A (Slide 35)

**Save as:** `docs/TECHNICAL_PRESENTATION_EXECUTIVE.md`

### 30-Minute Technical Overview

**Slides to include:**
1-10 (Intro, Architecture, Stack)
11-17 (Features & Phase 1)
26-30 (Testing & Security)
33-35 (Roadmap & Takeaways)

**Save as:** `docs/TECHNICAL_PRESENTATION_OVERVIEW.md`

### 60-Minute Deep Dive

**Use full presentation:** `docs/TECHNICAL_PRESENTATION.md`

Add:
- Live coding session (10 min)
- Interactive demo (15 min)
- Extended Q&A (15 min)

---

## Slide Design Tips

### Color Scheme

**Primary Colors:**
- #FF6600 (Adobe orange)
- #0066FF (Adobe blue)
- #FFFFFF (White)
- #000000 (Black)

### Fonts

**Headlines:** Arial Bold, 36-48pt
**Body:** Arial Regular, 18-24pt
**Code:** Consolas/Monaco, 14-16pt

### Layout

**Title Slides:**
- Large title (48pt)
- Subtitle (24pt)
- Minimal graphics

**Content Slides:**
- Title (36pt)
- 3-5 bullet points max
- One main visual per slide

**Code Slides:**
- Title (36pt)
- Well-formatted code block
- Brief explanation below

---

## Interactive Demo Script

### Demo 1: Basic Campaign Generation (5 min)

```bash
# 1. Show campaign brief
cat examples/campaign_brief.json

# 2. Run generation
./run_cli.sh examples/campaign_brief.json gemini

# 3. Show outputs
ls -la output/WIRELESS-EARBUDS-001/PREMIUM_TECH_2026/

# 4. Display generated asset
open output/WIRELESS-EARBUDS-001/PREMIUM_TECH_2026/en-US/1x1/*.png
```

### Demo 2: Phase 1 Features (5 min)

```bash
# 1. Generate campaign with Phase 1
./run_cli.sh examples/premium_tech_campaign_p1.json gemini

# 2. Show text customization in action
open output/*/PREMIUM_TECH_2026_P1/en-US/1x1/*.png

# 3. Compare with legacy version
# Side-by-side comparison of text effects
```

### Demo 3: Campaign Brief Generator (3 min)

```bash
# 1. List available presets
python3 scripts/generate_campaign_brief_p1_updates.py --list-presets

# 2. Generate campaign
python3 scripts/generate_campaign_brief_p1_updates.py \
  --template premium_tech \
  --text-preset readability_first \
  --post-preset vivid

# 3. Show generated JSON
cat examples/premium_tech_campaign_p1.json | jq '.text_customization'
```

---

## Appendix: Quick Commands

### Setup
```bash
# Install Marp
npm install -g @marp-team/marp-cli

# Install reveal-md
npm install -g reveal-md
```

### Generate Presentations
```bash
# PDF
marp docs/TECHNICAL_PRESENTATION.md --pdf -o presentations/tech.pdf

# PowerPoint
marp docs/TECHNICAL_PRESENTATION.md --pptx -o presentations/tech.pptx

# HTML
reveal-md docs/TECHNICAL_PRESENTATION.md --static presentations/html

# Preview
marp docs/TECHNICAL_PRESENTATION.md --preview
```

### Run Demos
```bash
# Basic campaign
./run_cli.sh examples/campaign_brief.json gemini

# Phase 1 campaign
./run_cli.sh examples/premium_tech_campaign_p1.json gemini

# Generate campaign brief
python3 scripts/generate_campaign_brief_p1_updates.py --template premium_tech
```

---

## Resources

**Documentation:**
- Full Technical Presentation: `docs/TECHNICAL_PRESENTATION.md`
- Phase 1 Guide: `docs/PHASE1_IMPLEMENTATION_GUIDE.md`
- Architecture: `docs/ARCHITECTURE.md`
- Features: `docs/FEATURES.md`

**Tools:**
- Marp: https://marp.app/
- reveal.js: https://revealjs.com/
- Slidev: https://sli.dev/

**Support:**
- GitHub Issues: https://github.com/yourusername/adobe-genai-project/issues
- Documentation: `/docs` directory

---

**Good luck with your presentation!**
