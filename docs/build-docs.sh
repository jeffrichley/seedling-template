#!/bin/bash
# Build and serve Seedling documentation using uv

set -e

# Ensure script runs from the docs directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ "$PWD" != "$SCRIPT_DIR" ]]; then
    cd "$SCRIPT_DIR"
fi

echo "🌱 Building Seedling documentation..."

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ uv is not installed. Please install uv first:"
    echo "   curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# Install dependencies using uv
echo "📥 Installing documentation dependencies..."
uv sync

# Build documentation
echo "🔨 Building HTML documentation..."
uv run make clean
uv run make html

echo "✅ Documentation built successfully!"
echo "📁 HTML files are in build/html/"
echo ""
echo "🌐 To serve locally, run:"
echo "   cd docs && make serve"
echo ""
echo "📖 Or open build/html/index.html in your browser"
