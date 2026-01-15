#!/bin/bash
# Activate virtual environment and run CLI

# Default values
DEFAULT_BRIEF="examples/campaign_brief2.json"
DEFAULT_BACKEND="gemini"

# Parse command-line arguments
BRIEF="${1:-$DEFAULT_BRIEF}"
BACKEND="${2:-$DEFAULT_BACKEND}"

# Show usage if --help or -h
if [[ "$1" == "--help" || "$1" == "-h" ]]; then
    echo "Usage: $0 [BRIEF_FILE] [BACKEND]"
    echo ""
    echo "Arguments:"
    echo "  BRIEF_FILE    Path to campaign brief JSON file (default: $DEFAULT_BRIEF)"
    echo "  BACKEND       Image generation backend: firefly, gemini, openai, dalle (default: $DEFAULT_BACKEND)"
    echo ""
    echo "Examples:"
    echo "  $0                                              # Use defaults"
    echo "  $0 examples/premium_tech_campaign.json          # Custom brief, default backend"
    echo "  $0 examples/premium_tech_campaign.json firefly  # Custom brief and backend"
    exit 0
fi

# Check if brief file exists
if [[ ! -f "$BRIEF" ]]; then
    echo "❌ Error: Campaign brief file not found: $BRIEF"
    echo "Run '$0 --help' for usage information"
    exit 1
fi

echo "📋 Campaign Brief: $BRIEF"
echo "🎨 Backend: $BACKEND"
echo ""

# Activate the venv
source venv/bin/activate

# Run the CLI command with provided arguments
python -m src.cli process --brief "$BRIEF" --backend "$BACKEND"

# Deactivate when done
deactivate
