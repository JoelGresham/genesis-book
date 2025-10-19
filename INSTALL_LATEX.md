# Installing LaTeX on WSL2 (Ubuntu)

## Option 1: Install LaTeX on WSL2 (Recommended)

### Quick Install (Essential Packages Only - ~500MB)

This installs just what you need for this book:

```bash
sudo apt-get update
sudo apt-get install -y texlive-latex-base texlive-fonts-recommended \
    texlive-fonts-extra texlive-latex-extra
```

**Time:** ~5-10 minutes depending on internet speed

### Full Install (All Packages - ~4GB)

This installs everything, preventing any missing package issues:

```bash
sudo apt-get update
sudo apt-get install -y texlive-full
```

**Time:** ~20-30 minutes depending on internet speed
**Space:** ~4GB

### After Installation

Test that it works:
```bash
pdflatex --version
```

Then build your book:
```bash
cd ~/projects/genesisBook
make
```

---

## Option 2: Use Overleaf (Online, No Installation)

If you don't want to install LaTeX locally, use Overleaf (free online LaTeX editor):

### Steps:

1. **Go to:** https://www.overleaf.com
2. **Sign up** for a free account
3. **Create New Project** → Upload Project
4. **Create a ZIP file:**
   ```bash
   cd ~/projects/genesisBook
   zip -r genesis_book.zip genesis_book.tex chapters_latex/
   ```
5. **Upload** the ZIP file to Overleaf
6. **Compile** - Overleaf will automatically compile and show the PDF
7. **Download** the finished PDF

**Pros:** No installation, works immediately, can edit online
**Cons:** Need internet, free account has limits

---

## Option 3: Use Docker (No Direct Installation)

If you have Docker installed:

```bash
cd ~/projects/genesisBook

# Run LaTeX in Docker container
docker run --rm -v "$PWD":/data \
    texlive/texlive:latest \
    pdflatex -interaction=nonstopmode genesis_book.tex

# Run twice for references
docker run --rm -v "$PWD":/data \
    texlive/texlive:latest \
    pdflatex -interaction=nonstopmode genesis_book.tex
```

---

## Option 4: Windows Native LaTeX

Since you're on WSL2, you can install LaTeX on Windows instead:

1. **Download MiKTeX:** https://miktex.org/download
2. **Install** (follow installer)
3. **Access from Windows:** Navigate to the project folder in Windows Explorer
4. **Compile:** Right-click `genesis_book.tex` → Compile with MiKTeX

---

## Recommended Approach

**For this project, I recommend Option 1 (Quick Install):**

```bash
# Update package list
sudo apt-get update

# Install essential LaTeX packages
sudo apt-get install -y texlive-latex-base texlive-fonts-recommended \
    texlive-fonts-extra texlive-latex-extra

# Verify installation
pdflatex --version

# Build your book
cd ~/projects/genesisBook
make
```

This will take about 5-10 minutes and use about 500MB of disk space.

---

## Troubleshooting

### "Unable to locate package"

Update your package list:
```bash
sudo apt-get update
```

### Missing Fonts Error

Install additional fonts:
```bash
sudo apt-get install texlive-fonts-extra
```

### Missing Package Error

Install the specific package (replace `packagename`):
```bash
sudo apt-get install texlive-latex-extra
```

### Out of Space

Check available space:
```bash
df -h
```

If low, use Option 2 (Overleaf) instead.

---

## What Gets Installed

**texlive-latex-base:** Core LaTeX engine
**texlive-fonts-recommended:** Standard fonts
**texlive-fonts-extra:** Additional fonts (including EB Garamond)
**texlive-latex-extra:** Extra packages (titlesec, fancyhdr, etc.)

---

## Alternative: Build on Windows Directly

If you prefer not to use WSL for this:

1. **Install MiKTeX** on Windows: https://miktex.org/download
2. **Open Windows Terminal** or CMD
3. **Navigate** to your project (in Windows path):
   ```cmd
   cd C:\Users\YourName\projects\genesisBook
   ```
4. **Compile:**
   ```cmd
   pdflatex genesis_book.tex
   pdflatex genesis_book.tex
   ```

---

## Quick Decision Tree

**Have fast internet?** → Use Overleaf (Option 2)
**Want local builds?** → Install on WSL2 (Option 1)
**Have Docker?** → Use Docker (Option 3)
**Prefer Windows?** → Install MiKTeX (Option 4)

---

## Next Steps After Installation

Once LaTeX is installed:

```bash
cd ~/projects/genesisBook
make              # Build the book
make view         # Build and open (if you have a PDF viewer)
ls -lh *.pdf      # Check the file size
```

Your `genesis_book.pdf` should be 1-2 MB and 400-500 pages!
