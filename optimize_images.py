#!/usr/bin/env python3
"""
Optimize chapter images for print book:
1. Remove background
2. Resize to optimal print resolution (300 DPI)
3. Compress to reduce file size
"""

import os
import glob
import subprocess
from PIL import Image

# Configuration
INPUT_DIR = "images/chapterImages"
OUTPUT_DIR = "images/chapterImages_optimized"
BACKUP_DIR = "images/chapterImages_backup"

# Target specs for 6x9 book with margins
# Usable width ~5 inches at 300 DPI = 1500 pixels
TARGET_WIDTH = 1500
TARGET_DPI = 300

def setup_directories():
    """Create necessary directories"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(BACKUP_DIR, exist_ok=True)
    print(f"Created directories:")
    print(f"  - Output: {OUTPUT_DIR}")
    print(f"  - Backup: {BACKUP_DIR}")

def get_image_files():
    """Get all PNG files from input directory"""
    files = sorted(glob.glob(f"{INPUT_DIR}/*.png"))
    return files

def remove_background(input_path, output_path):
    """Remove background using rembg"""
    print(f"    Removing background...")
    try:
        # Run rembg command
        result = subprocess.run(
            ['rembg', 'i', input_path, output_path],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode != 0:
            print(f"    Warning: rembg had issues: {result.stderr}")
            return False
        return True
    except subprocess.TimeoutExpired:
        print(f"    Warning: rembg timed out")
        return False
    except Exception as e:
        print(f"    Warning: rembg failed: {e}")
        return False

def optimize_image(input_path, output_path):
    """Optimize image: resize and compress"""
    print(f"    Optimizing size and resolution...")

    try:
        img = Image.open(input_path)

        # Get current size
        original_width, original_height = img.size
        print(f"      Original: {original_width}x{original_height}")

        # Calculate new height maintaining aspect ratio
        if original_width > TARGET_WIDTH:
            ratio = TARGET_WIDTH / original_width
            new_height = int(original_height * ratio)

            # Resize with high-quality resampling
            img = img.resize((TARGET_WIDTH, new_height), Image.Resampling.LANCZOS)
            print(f"      Resized to: {TARGET_WIDTH}x{new_height}")
        else:
            print(f"      No resize needed (already optimal)")

        # Set DPI metadata
        img.info['dpi'] = (TARGET_DPI, TARGET_DPI)

        # Save with optimization
        img.save(output_path, 'PNG', optimize=True, dpi=(TARGET_DPI, TARGET_DPI))

        return True
    except Exception as e:
        print(f"    Error optimizing: {e}")
        return False

def get_file_size_mb(filepath):
    """Get file size in MB"""
    return os.path.getsize(filepath) / (1024 * 1024)

def process_image(input_path):
    """Process a single image: remove bg and optimize"""
    filename = os.path.basename(input_path)
    temp_path = os.path.join(OUTPUT_DIR, f"temp_{filename}")
    output_path = os.path.join(OUTPUT_DIR, filename)

    print(f"\n  Processing: {filename}")

    original_size = get_file_size_mb(input_path)
    print(f"    Original size: {original_size:.2f} MB")

    # Step 1: Remove background
    if remove_background(input_path, temp_path):
        # Step 2: Optimize
        if optimize_image(temp_path, output_path):
            # Clean up temp file
            if os.path.exists(temp_path):
                os.remove(temp_path)

            final_size = get_file_size_mb(output_path)
            print(f"    Final size: {final_size:.2f} MB")
            print(f"    Savings: {original_size - final_size:.2f} MB ({((original_size - final_size) / original_size * 100):.1f}%)")
            return True
        else:
            print(f"    Failed to optimize, using original")
            # If optimization fails, just copy original
            subprocess.run(['cp', input_path, output_path])
    else:
        # If background removal fails, just optimize original
        print(f"    Background removal failed, optimizing original...")
        if optimize_image(input_path, output_path):
            final_size = get_file_size_mb(output_path)
            print(f"    Final size: {final_size:.2f} MB")
            return True

    return False

def main():
    """Main processing function"""
    print("="*70)
    print("Image Optimization for The Genesis Code")
    print("="*70)

    # Setup
    setup_directories()

    # Get images
    image_files = get_image_files()
    print(f"\nFound {len(image_files)} images to process")

    if not image_files:
        print("No images found!")
        return

    # Calculate total original size
    total_original = sum(get_file_size_mb(f) for f in image_files)
    print(f"Total original size: {total_original:.2f} MB")

    # Process each image
    print("\n" + "="*70)
    print("Processing images...")
    print("="*70)

    success_count = 0
    for image_path in image_files:
        if process_image(image_path):
            success_count += 1

    # Calculate final stats
    output_files = glob.glob(f"{OUTPUT_DIR}/*.png")
    total_final = sum(get_file_size_mb(f) for f in output_files)

    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    print(f"Processed: {success_count}/{len(image_files)} images")
    print(f"Original total size: {total_original:.2f} MB")
    print(f"Optimized total size: {total_final:.2f} MB")
    print(f"Total savings: {total_original - total_final:.2f} MB ({((total_original - total_final) / total_original * 100):.1f}%)")
    print(f"\nOptimized images saved to: {OUTPUT_DIR}/")
    print("\nNext steps:")
    print("1. Review optimized images to ensure quality")
    print("2. If satisfied, backup originals and replace:")
    print(f"   mv {INPUT_DIR} {BACKUP_DIR}/")
    print(f"   mv {OUTPUT_DIR} {INPUT_DIR}")

if __name__ == "__main__":
    main()
