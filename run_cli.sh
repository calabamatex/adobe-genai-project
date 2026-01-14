#!/bin/bash
# Activate virtual environment and run CLI

# Activate the venv
source venv/bin/activate

# Run the CLI command with correct backend name
python -m src.cli process --brief examples/campaign_brief2.json --backend gemini

# Deactivate when done
deactivate
