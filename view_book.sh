#!/bin/bash

# Quick script to view or copy your book

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║           The Genesis Code - View Your Book              ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

PDF_FILE="genesis_book.pdf"

if [ ! -f "$PDF_FILE" ]; then
    echo "❌ PDF not found. Run 'make' first to build your book."
    exit 1
fi

echo "✅ Book found: $PDF_FILE"
echo "   Size: $(du -h $PDF_FILE | cut -f1)"
echo "   Pages: 369"
echo ""
echo "Choose an option:"
echo ""
echo "  1) Copy to Windows Desktop"
echo "  2) Copy to Windows Downloads"
echo "  3) Show file location (for manual access)"
echo "  4) Try to open with default viewer"
echo "  5) Exit"
echo ""
read -p "Enter choice [1-5]: " choice

case $choice in
    1)
        DEST="/mnt/c/Users/$USER/Desktop/genesis_book.pdf"
        if [ -d "/mnt/c/Users/$USER/Desktop" ]; then
            cp "$PDF_FILE" "$DEST"
            echo "✅ Copied to Desktop: $DEST"
        else
            echo "❌ Desktop not found. Try option 3 for manual access."
        fi
        ;;
    2)
        DEST="/mnt/c/Users/$USER/Downloads/genesis_book.pdf"
        if [ -d "/mnt/c/Users/$USER/Downloads" ]; then
            cp "$PDF_FILE" "$DEST"
            echo "✅ Copied to Downloads: $DEST"
        else
            echo "❌ Downloads not found. Try option 3 for manual access."
        fi
        ;;
    3)
        echo ""
        echo "📍 File Locations:"
        echo ""
        echo "   WSL Path:"
        echo "   $(pwd)/$PDF_FILE"
        echo ""
        echo "   Windows Path:"
        echo "   \\\\wsl\$\\Ubuntu$(pwd | sed 's|/mnt/c|\\c:|g' | tr '/' '\\')\\$PDF_FILE"
        echo ""
        echo "   Or use Windows File Explorer and navigate to:"
        echo "   \\\\wsl\$\\Ubuntu\\home\\gresh\\projects\\genesisBook"
        echo ""
        ;;
    4)
        if command -v xdg-open &> /dev/null; then
            xdg-open "$PDF_FILE" 2>/dev/null &
            echo "✅ Opening with default viewer..."
        elif command -v explorer.exe &> /dev/null; then
            explorer.exe "$(wslpath -w "$PDF_FILE")" 2>/dev/null &
            echo "✅ Opening with Windows Explorer..."
        else
            echo "❌ No viewer found. Use option 3 for manual access."
        fi
        ;;
    5)
        echo "Goodbye!"
        exit 0
        ;;
    *)
        echo "Invalid choice."
        ;;
esac

echo ""
echo "📚 Your 369-page book is ready for publishing!"
echo ""
