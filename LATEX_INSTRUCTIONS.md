# The Genesis Code - LaTeX Book Compilation Guide

## Overview

This directory contains the complete LaTeX source for "The Genesis Code," professionally formatted as a 6"×9" trade paperback novel.

## Directory Structure

```
genesisBook/
├── genesis_book.tex          # Main LaTeX file (compile this)
├── chapters/                  # Original markdown chapters
├── chapters_latex/            # Converted LaTeX chapters
├── convert_to_latex.py        # Chapter conversion script
├── LATEX_INSTRUCTIONS.md      # This file
└── genesis_book.pdf           # Generated PDF (after compilation)
```

## Requirements

### Required LaTeX Packages

The template uses the following packages (install via your LaTeX distribution):

- **Core:** `book` class, `inputenc`, `fontenc`, `babel`
- **Layout:** `geometry`, `fancyhdr`, `titlesec`
- **Typography:** `ebgaramond`, `cabin`, `microtype`, `setspace`
- **Utilities:** `graphicx`, `xcolor`, `hyperref`, `csquotes`, `nowidow`

### LaTeX Distribution

You need a complete LaTeX distribution. Choose one:

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install texlive-full
```

**macOS:**
```bash
brew install --cask mactex
```

**Windows:**
Download and install [MiKTeX](https://miktex.org/) or [TeX Live](https://www.tug.org/texlive/)

## Compilation Instructions

### Method 1: Basic Compilation

```bash
cd /home/gresh/projects/genesisBook

# First pass - generates structure
pdflatex genesis_book.tex

# Second pass - resolves references
pdflatex genesis_book.tex

# Optional third pass for table of contents
pdflatex genesis_book.tex
```

### Method 2: Using latexmk (Recommended)

```bash
latexmk -pdf -interaction=nonstopmode genesis_book.tex
```

This automatically runs LaTeX the correct number of times.

### Method 3: Full Build with Cleanup

```bash
# Compile
pdflatex genesis_book.tex
pdflatex genesis_book.tex

# Clean auxiliary files
rm -f *.aux *.log *.toc *.out *.lot *.lof
```

## Book Specifications

### Physical Dimensions
- **Format:** Trade Paperback
- **Size:** 6" × 9" (standard fiction size)
- **Page Count:** ~400-500 pages (estimated)

### Typography
- **Body Font:** EB Garamond 12pt (professional book serif)
- **Headers:** Cabin (clean sans-serif)
- **Line Spacing:** 1.2 (professional fiction standard)
- **Margins:**
  - Top: 0.75"
  - Bottom: 0.75"
  - Inner: 0.75" (binding edge)
  - Outer: 0.5"

### Structure
- **Part One:** Chapters 1-15 (The Architects, 65 million years ago)
- **Part Two:** Chapters 16-32 (The Inheritors, present day)
- **Epilogue:** Chapter 33 (The Cycle, far future)

## Customization

### Changing Fonts

Edit `genesis_book.tex` around line 28-30:

```latex
\usepackage{ebgaramond}  % Change to \usepackage{palatino} or others
\usepackage[sfdefault]{cabin}  % Change to other sans-serif fonts
```

### Adjusting Page Size

Edit `genesis_book.tex` around line 18-26:

```latex
\usepackage[
    paperwidth=6in,      % Change width
    paperheight=9in,     % Change height
    top=0.75in,          % Adjust margins
    bottom=0.75in,
    inner=0.75in,
    outer=0.5in,
]{geometry}
```

### Scene Break Styling

The `\scenebreak` command is defined around line 142:

```latex
\newcommand{\scenebreak}{%
    \vspace{1em}%
    \noindent\hfil{* * *}\hfil%
    \vspace{1em}%
}
```

Change `* * *` to any symbol you prefer.

## Reconverting Chapters

If you modify the markdown chapters, reconvert them:

```bash
python3 convert_to_latex.py
```

This will regenerate all files in `chapters_latex/`.

## Troubleshooting

### Missing Packages

If you get errors about missing packages:

```bash
# Ubuntu/Debian
sudo apt-get install texlive-fonts-extra texlive-latex-extra

# Or install specific package
sudo tlmgr install ebgaramond
```

### Compilation Errors

1. **Check the log:** Look at `genesis_book.log` for detailed errors
2. **Run with errors:** `pdflatex -interaction=nonstopmode genesis_book.tex`
3. **Clean and rebuild:**
   ```bash
   rm -f *.aux *.toc *.out *.log
   pdflatex genesis_book.tex
   ```

### Font Issues

If EB Garamond doesn't work:

1. Replace in `genesis_book.tex`:
   ```latex
   % \usepackage{ebgaramond}  % Comment out
   \usepackage{times}          % Use Times instead
   ```

### Page Numbers Not Showing

Run LaTeX at least twice:
```bash
pdflatex genesis_book.tex
pdflatex genesis_book.tex
```

## Print-Ready PDF

To create a print-ready PDF for publishing:

### 1. Compile with High Quality

```bash
pdflatex -interaction=batchmode genesis_book.tex
pdflatex -interaction=batchmode genesis_book.tex
```

### 2. Check PDF Settings

The generated PDF includes:
- Embedded fonts
- Proper page dimensions (6"×9")
- Correct margins for binding
- Hyperlinked table of contents (invisible in print)

### 3. Verify Before Printing

- **Page count:** Should be divisible by 4 for perfect binding
- **Bleed:** Add 0.125" bleed if required by your printer
- **Color mode:** Convert to grayscale if printing black & white
- **Resolution:** Ensure any images are 300+ DPI

## Professional Publishing

### KDP (Kindle Direct Publishing)

1. Use the generated PDF as interior file
2. Set trim size to 6"×9"
3. Paper type: Cream or White
4. Cover: Upload separately (not included)

### IngramSpark

1. PDF meets their requirements
2. May need to adjust margins slightly
3. Consider their specific trim size options

### Print on Demand Services

Compatible with:
- Lulu
- BookBaby
- Blurb
- Most POD services accepting standard PDF

## Advanced Features

### Adding Epigraphs

Use the `\chapterquote` command:

```latex
\chapter{Chapter Title}
\chapterquote{Quote text here}{Author Name}

Chapter content...
```

### Custom Headers

Edit the fancy header settings around line 135:

```latex
\fancyhead[LE]{\small\itshape\nouppercase{\leftmark}}
\fancyhead[RO]{\small\itshape The Genesis Code}
```

### ISBN and Copyright

Edit the copyright page section around line 218:

```latex
ISBN: [Your ISBN here]
```

## Quality Checklist

Before final print:

- [ ] Compile at least twice for proper references
- [ ] Review table of contents
- [ ] Check all chapter breaks are correct
- [ ] Verify scene breaks appear correctly
- [ ] Ensure no orphaned/widowed lines
- [ ] Check margins and page numbers
- [ ] Review font rendering
- [ ] Verify PDF is correct page size
- [ ] Test print a single copy first

## File Sizes

- **LaTeX source:** ~2-3 MB total
- **Generated PDF:** ~1-2 MB (text only, no images)
- **With images:** Depends on image count/quality

## Support and Issues

If you encounter problems:

1. Check `genesis_book.log` for errors
2. Verify all packages are installed
3. Try compiling individual chapters first
4. Use `pdflatex -interaction=errorstopmode` for detailed debugging

## License

The Genesis Code © 2025. All rights reserved.

---

**Last Updated:** 2025-10-19
**Template Version:** 1.0
**LaTeX Engine:** pdfLaTeX
