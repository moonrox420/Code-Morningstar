#!/bin/bash
# Code Morningstar Unix/Linux/macOS Deployment Script
echo "🌟 Code Morningstar Unix Deployment"
echo "===================================="

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed or not in PATH"
    echo "Please install Python 3.8+ and try again"
    exit 1
fi

# Run the Python deployment script
python3 deploy.py
