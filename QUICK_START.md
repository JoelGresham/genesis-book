# The Genesis Code - Quick Start Guide

## Fastest Way to Generate Your Book

### 1. One-Command Build

```bash
cd /home/gresh/projects/genesisBook
make
```

That's it! This will create `genesis_book.pdf`.

### 2. Build and View

```bash
make view
```

Compiles the book and opens it automatically.

---

## What You Get

- **Professional 6"×9" trade paperback format**
- **~400-500 page novel** with proper typography
- **Print-ready PDF** for self-publishing
- **All 33 chapters** formatted and ready

---

## File Overview

| File | Purpose |
|------|---------|
| `genesis_book.tex` | Main LaTeX source file |
| `chapters_latex/` | All 33 chapters in LaTeX format |
| `Makefile` | Build automation |
| `genesis_book.pdf` | Your finished book (after compilation) |

---

## Common Tasks

### Build the book
```bash
make
```

### Rebuild from scratch
```bash
make rebuild
```

### Edit a chapter
1. Edit the chapter in `chapters/chapter_XX.md`
2. Run: `make convert`
3. Run: `make`

### Clean up temporary files
```bash
make clean
```

---

## Requirements

You need LaTeX installed:

**Ubuntu/Debian:**
```bash
sudo apt-get install texlive-full
```

**macOS:**
```bash
brew install --cask mactex
```

**Windows:**
Download [MiKTeX](https://miktex.org/)

---

## Customization

All settings are in `genesis_book.tex`:

- **Page size:** Line 18-26 (currently 6"×9")
- **Fonts:** Line 28-30 (EB Garamond + Cabin)
- **Margins:** Line 20-25
- **Title page:** Line 215-230
- **Copyright:** Line 235-250

---

## Publishing Ready

The generated PDF is ready for:
- ✅ Kindle Direct Publishing (KDP)
- ✅ IngramSpark
- ✅ Lulu, BookBaby, etc.
- ✅ Professional printing services

Just upload `genesis_book.pdf` as your interior file!

---

## Book Statistics

- **Total Chapters:** 33
- **Estimated Word Count:** ~128,000 words
- **Part One (Dinosaurs):** Chapters 1-15
- **Part Two (Humans):** Chapters 16-32
- **Epilogue:** Chapter 33

---

## Need Help?

1. Check `LATEX_INSTRUCTIONS.md` for detailed guide
2. Run `make help` for all available commands
3. Check `genesis_book.log` if compilation fails

---

## Pro Tips

🔥 **Use `make view`** to automatically open PDF after building

🔥 **Run `make check`** to validate LaTeX without generating PDF

🔥 **Use `make wordcount`** to estimate total word count

---

That's all you need to know! Run `make` and you'll have a beautiful, print-ready book.
