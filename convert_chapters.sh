#!/bin/bash

# Script to convert markdown chapters to LaTeX format
# Handles the Genesis Code book chapters

CHAPTERS_DIR="chapters"
LATEX_DIR="chapters_latex"

# Create LaTeX directory if it doesn't exist
mkdir -p "$LATEX_DIR"

echo "Converting markdown chapters to LaTeX format..."

# Process each chapter
for md_file in "$CHAPTERS_DIR"/chapter_*.md; do
    # Skip summary files
    if [[ "$md_file" == *"_summary.md" ]]; then
        continue
    fi

    # Get base filename
    basename=$(basename "$md_file" .md)
    tex_file="$LATEX_DIR/${basename}.tex"

    echo "Processing $basename..."

    # Use pandoc for conversion with custom settings
    pandoc "$md_file" \
        -f markdown \
        -t latex \
        --wrap=preserve \
        --top-level-division=chapter \
        -o "$tex_file"

    # Post-process the LaTeX file to improve formatting
    # Remove \chapter commands (we'll add them in the main file)
    # Fix common issues
    sed -i 's/\\chapter{/\\chapter*{/g' "$tex_file"
    sed -i 's/\\hypertarget{[^}]*}{}//g' "$tex_file"
    sed -i 's/\\section/\\section*/g' "$tex_file"

    # Fix em-dashes and quotes
    sed -i 's/---/\\emdash{}/g' "$tex_file"
    sed -i "s/'/'/g" "$tex_file"
    sed -i 's/"/``/g' "$tex_file"
    sed -i 's/"/'"'"'/g' "$tex_file"

    # Fix scene breaks (horizontal rules in markdown become scene breaks)
    sed -i 's/\\begin{center}\\rule{0.5\\linewidth}{0.5pt}\\end{center}/\\scenebreak/g' "$tex_file"
    sed -i 's/---/\\scenebreak/g' "$tex_file"

done

echo "Conversion complete! LaTeX files are in $LATEX_DIR/"
echo ""
echo "Note: You may need to manually review and adjust:"
echo "  - Scene breaks (look for horizontal rules or '---')"
echo "  - Dialogue formatting"
echo "  - Special characters"
