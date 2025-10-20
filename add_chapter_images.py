#!/usr/bin/env python3
"""
Script to add images to chapter markdown files.
Processes one chapter at a time to avoid API size limits.
"""

import os
import glob
import re

# Configuration
CHAPTERS_DIR = "chapters"
IMAGES_DIR = "images/chapterImages"

def get_chapter_number(chapter_file):
    """Extract chapter number from filename like 'chapter_01.md'"""
    match = re.search(r'chapter_(\d+)', chapter_file)
    if match:
        return int(match.group(1))
    return None

def get_available_images():
    """Get list of all available images sorted by number"""
    image_files = glob.glob(f"{IMAGES_DIR}/*.png")
    return sorted(image_files)

def add_image_to_chapter(chapter_file, image_file):
    """Add image reference to the top of a chapter file"""

    # Read the chapter content
    with open(chapter_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if image already exists
    if '![Chapter Image]' in content or f'images/chapterImages' in content:
        print(f"  Image already present in {os.path.basename(chapter_file)}")
        return False

    # Find the chapter title (first line starting with #)
    lines = content.split('\n')
    title_line_idx = -1

    for idx, line in enumerate(lines):
        if line.strip().startswith('# Chapter'):
            title_line_idx = idx
            break

    if title_line_idx == -1:
        print(f"  Warning: No chapter title found in {os.path.basename(chapter_file)}")
        return False

    # Get relative path for the image
    image_rel_path = os.path.join('../', image_file)

    # Insert image after title with proper spacing
    image_markdown = f"\n![Chapter Image]({image_rel_path})\n"

    # Insert after title line
    lines.insert(title_line_idx + 1, image_markdown)

    # Write back
    new_content = '\n'.join(lines)

    with open(chapter_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def main():
    """Main function to process chapters"""

    # Get all chapter files
    chapter_files = sorted(glob.glob(f"{CHAPTERS_DIR}/chapter_*.md"))

    # Filter out summary files
    chapter_files = [f for f in chapter_files if 'summary' not in f.lower()]

    print(f"Found {len(chapter_files)} chapters")

    # Get available images
    images = get_available_images()
    print(f"Found {len(images)} images")

    if len(images) < len(chapter_files):
        print(f"\nWarning: Only {len(images)} images for {len(chapter_files)} chapters")
        print("Will assign images to first chapters only")

    # Process each chapter
    updated_count = 0
    for idx, chapter_file in enumerate(chapter_files):
        if idx >= len(images):
            print(f"\nNo more images available for {os.path.basename(chapter_file)}")
            break

        chapter_num = get_chapter_number(chapter_file)
        image_file = images[idx]

        print(f"\nProcessing Chapter {chapter_num}: {os.path.basename(chapter_file)}")
        print(f"  Using image: {os.path.basename(image_file)}")

        if add_image_to_chapter(chapter_file, image_file):
            updated_count += 1
            print(f"  ✓ Image added successfully")

    print(f"\n{'='*60}")
    print(f"Complete! Updated {updated_count} chapters with images")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
