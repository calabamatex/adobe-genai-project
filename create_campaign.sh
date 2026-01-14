#!/bin/bash
# Quick campaign generator script

# Activate virtual environment
source venv/bin/activate

# Generate new campaign
python -m src.cli new-campaign "$@"

# Deactivate when done
deactivate
