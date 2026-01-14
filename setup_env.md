# API Key Setup Instructions

## Step 1: Get API Keys

1. **Claude API Key** (Anthropic)
   - Sign up at: https://console.anthropic.com/
   - Navigate to: API Keys section
   - Create a new API key

2. **OpenAI API Key**
   - Sign up at: https://platform.openai.com/
   - Navigate to: API Keys section
   - Create a new API key

## Step 2: Create .env File

Copy the example and add your keys:

```bash
cp .env.example .env
```

Then edit `.env` and replace the placeholder values:

```bash
# Required for guideline extraction
CLAUDE_API_KEY=sk-ant-api03-your-actual-claude-key-here

# Required for OpenAI backend
OPENAI_API_KEY=sk-your-actual-openai-key-here

# Other settings (optional)
DEFAULT_IMAGE_BACKEND=openai
OUTPUT_DIR=./output
```

## Step 3: Run the CLI

```bash
source venv/bin/activate
python -m src.cli process --brief examples/campaign_brief.json --backend openai
```

## Alternative: Test Without API Keys

Run the test suite (uses mocks, no API keys needed):
```bash
source venv/bin/activate
pytest -v
```

Or use dry-run mode (if available):
```bash
python -m src.cli process --brief examples/campaign_brief.json --backend openai --dry-run
```
