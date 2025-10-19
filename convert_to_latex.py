#!/usr/bin/env python3
"""
Convert Genesis Code markdown chapters to LaTeX format.
Handles scene breaks, dialogue, and proper formatting.
"""

import os
import re
from pathlib import Path


def escape_latex(text):
    """Escape special LaTeX characters."""
    # Order matters!
    replacements = [
        ('\\', r'\textbackslash{}'),
        ('&', r'\&'),
        ('%', r'\%'),
        ('$', r'\$'),
        ('#', r'\#'),
        ('_', r'\_'),
        ('{', r'\{'),
        ('}', r'\}'),
        ('~', r'\textasciitilde{}'),
        ('^', r'\textasciicircum{}'),
    ]

    for old, new in replacements:
        text = text.replace(old, new)

    return text


def process_markdown_to_latex(md_content, chapter_num):
    """Convert markdown content to LaTeX."""

    lines = md_content.split('\n')
    tex_lines = []
    in_dialogue = False

    for i, line in enumerate(lines):
        # Skip the markdown chapter heading (line 1: # Chapter X: Title)
        if i == 0 and line.startswith('# Chapter'):
            continue

        # Handle scene breaks (horizontal rules or standalone ---)
        if line.strip() in ['---', '* * *', '***'] or line.startswith('---'):
            tex_lines.append('')
            tex_lines.append(r'\scenebreak')
            tex_lines.append('')
            continue

        # Handle blank lines
        if not line.strip():
            tex_lines.append('')
            continue

        # Handle block quotes (lines starting with >)
        if line.strip().startswith('>'):
            quoted = line.strip()[1:].strip()
            # Don't escape the content if it looks like it might already be LaTeX
            if not quoted.startswith('\\'):
                quoted = escape_latex(quoted)
            tex_lines.append(r'\begin{quote}')
            tex_lines.append(r'\itshape ' + quoted)
            tex_lines.append(r'\end{quote}')
            continue

        # Regular paragraph - escape and add
        processed = escape_latex(line)

        # Fix common replacements that were over-escaped
        processed = processed.replace(r'\textbackslash{}emdash', r'\emdash')
        processed = processed.replace(r'\textbackslash{}scenebreak', r'\scenebreak')

        tex_lines.append(processed)

    # Join lines and clean up
    tex_content = '\n'.join(tex_lines)

    # Fix multiple blank lines
    tex_content = re.sub(r'\n{3,}', '\n\n', tex_content)

    return tex_content


def convert_chapter(md_file, tex_file):
    """Convert a single markdown chapter to LaTeX."""

    # Read markdown
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Extract chapter number from filename
    chapter_match = re.search(r'chapter_(\d+)', str(md_file))
    chapter_num = chapter_match.group(1) if chapter_match else '00'

    # Extract chapter title from first line
    first_line = md_content.split('\n')[0]
    title_match = re.search(r'# Chapter \d+: (.+)', first_line)
    if title_match:
        chapter_title = title_match.group(1)
    else:
        chapter_title = f"Chapter {chapter_num}"

    # Convert content
    tex_content = process_markdown_to_latex(md_content, chapter_num)

    # Add chapter heading
    full_tex = f"\\chapter{{{chapter_title}}}\n\\label{{ch:{chapter_num}}}\n\n{tex_content}\n"

    # Write LaTeX
    with open(tex_file, 'w', encoding='utf-8') as f:
        f.write(full_tex)

    print(f"Converted: {md_file.name} -> {tex_file.name}")


def main():
    """Main conversion function."""

    # Setup directories
    chapters_dir = Path('chapters')
    latex_dir = Path('chapters_latex')
    latex_dir.mkdir(exist_ok=True)

    print("Converting Genesis Code chapters to LaTeX...\n")

    # Get all chapter markdown files (excluding summaries)
    chapter_files = sorted([
        f for f in chapters_dir.glob('chapter_*.md')
        if '_summary' not in f.name
    ])

    print(f"Found {len(chapter_files)} chapters to convert\n")

    # Convert each chapter
    for md_file in chapter_files:
        tex_file = latex_dir / f"{md_file.stem}.tex"
        try:
            convert_chapter(md_file, tex_file)
        except Exception as e:
            print(f"Error converting {md_file.name}: {e}")

    print(f"\nConversion complete!")
    print(f"LaTeX files saved to: {latex_dir}/")
    print(f"\nNext steps:")
    print(f"1. Review converted files in {latex_dir}/")
    print(f"2. Update genesis_book.tex to use chapters_latex/ directory")
    print(f"3. Run: pdflatex genesis_book.tex")
    print(f"4. Run again for proper references: pdflatex genesis_book.tex")


if __name__ == '__main__':
    main()
