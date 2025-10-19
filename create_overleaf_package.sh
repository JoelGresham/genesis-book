#!/bin/bash

# Create Overleaf-ready package
# This creates a ZIP file you can upload to Overleaf.com

echo "Creating Overleaf package for The Genesis Code..."
echo ""

# Package name
PACKAGE_NAME="genesis_code_overleaf.zip"

# Remove old package if exists
rm -f "$PACKAGE_NAME"

# Create the ZIP with all necessary files
zip -r "$PACKAGE_NAME" \
    genesis_book.tex \
    chapters_latex/ \
    -x "*.aux" "*.log" "*.toc" "*.out" "*.pdf"

echo ""
echo "✓ Package created: $PACKAGE_NAME"
echo ""
echo "Next steps:"
echo "1. Go to https://www.overleaf.com"
echo "2. Sign up/login (free)"
echo "3. Click 'New Project' → 'Upload Project'"
echo "4. Upload the file: $PACKAGE_NAME"
echo "5. Overleaf will compile automatically!"
echo "6. Download your PDF when ready"
echo ""
echo "File location: $(pwd)/$PACKAGE_NAME"
echo "File size: $(du -h $PACKAGE_NAME | cut -f1)"
