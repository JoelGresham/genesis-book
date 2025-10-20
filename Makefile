# Makefile for Aurelia LaTeX compilation
# Usage: make [target]

# Main LaTeX file
MAIN = aurelia
TEX_FILE = $(MAIN).tex
PDF_FILE = $(MAIN).pdf

# LaTeX compiler
LATEX = pdflatex
LATEX_FLAGS = -interaction=nonstopmode -halt-on-error

# Auxiliary file extensions to clean
AUX_EXTS = aux log toc out lof lot bbl blg idx ind ilg

# Default target
.PHONY: all
all: $(PDF_FILE)

# Compile the PDF (runs LaTeX twice for references)
$(PDF_FILE): $(TEX_FILE)
	@echo "Compiling $(TEX_FILE) (first pass)..."
	$(LATEX) $(LATEX_FLAGS) $(TEX_FILE)
	@echo "Compiling $(TEX_FILE) (second pass)..."
	$(LATEX) $(LATEX_FLAGS) $(TEX_FILE)
	@echo "PDF generated: $(PDF_FILE)"

# Force rebuild (clean then compile)
.PHONY: rebuild
rebuild: clean all

# Convert markdown chapters to LaTeX
.PHONY: convert
convert:
	@echo "Converting markdown chapters to LaTeX..."
	python3 convert_to_latex.py
	@echo "Conversion complete!"

# Clean auxiliary files
.PHONY: clean
clean:
	@echo "Cleaning auxiliary files..."
	@for ext in $(AUX_EXTS); do \
		rm -f $(MAIN).$$ext; \
	done
	@rm -f chapters_latex/*.aux
	@echo "Clean complete!"

# Full clean (including PDF)
.PHONY: distclean
distclean: clean
	@echo "Removing generated PDF..."
	@rm -f $(PDF_FILE)
	@echo "Full clean complete!"

# View the PDF (works on Linux with xdg-open)
.PHONY: view
view: $(PDF_FILE)
	@if command -v xdg-open > /dev/null; then \
		xdg-open $(PDF_FILE); \
	elif command -v open > /dev/null; then \
		open $(PDF_FILE); \
	else \
		echo "No PDF viewer found. Please open $(PDF_FILE) manually."; \
	fi

# Quick compile without stopping on errors
.PHONY: quick
quick:
	@echo "Quick compiling $(TEX_FILE)..."
	$(LATEX) -interaction=batchmode $(TEX_FILE)
	@echo "Quick compile complete!"

# Full compilation with three passes (for complex references)
.PHONY: full
full: $(TEX_FILE)
	@echo "Full compilation (3 passes)..."
	$(LATEX) $(LATEX_FLAGS) $(TEX_FILE)
	$(LATEX) $(LATEX_FLAGS) $(TEX_FILE)
	$(LATEX) $(LATEX_FLAGS) $(TEX_FILE)
	@echo "Full compilation complete!"

# Check for LaTeX errors without generating PDF
.PHONY: check
check:
	@echo "Checking $(TEX_FILE) for errors..."
	$(LATEX) -draftmode $(LATEX_FLAGS) $(TEX_FILE)
	@echo "Check complete!"

# Show word count estimate
.PHONY: wordcount
wordcount:
	@echo "Estimating word count from LaTeX chapters..."
	@wc -w chapters_latex/*.tex | tail -n 1
	@echo "(Note: This includes LaTeX commands, actual count is ~70% of this)"

# Show help
.PHONY: help
help:
	@echo "Aurelia - LaTeX Compilation"
	@echo ""
	@echo "Available targets:"
	@echo "  make          - Compile the book (default, runs LaTeX twice)"
	@echo "  make all      - Same as default"
	@echo "  make rebuild  - Clean then compile"
	@echo "  make convert  - Convert markdown chapters to LaTeX"
	@echo "  make clean    - Remove auxiliary files"
	@echo "  make distclean- Remove all generated files including PDF"
	@echo "  make view     - Compile and open the PDF"
	@echo "  make quick    - Quick compile (batch mode, one pass)"
	@echo "  make full     - Full compile (three passes)"
	@echo "  make check    - Check for LaTeX errors without PDF"
	@echo "  make wordcount- Show estimated word count"
	@echo "  make help     - Show this help message"
	@echo ""
	@echo "Examples:"
	@echo "  make              # Build the book"
	@echo "  make view         # Build and view"
	@echo "  make rebuild      # Clean build from scratch"
	@echo "  make convert all  # Reconvert chapters and build"
