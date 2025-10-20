#!/usr/bin/env python3
"""
Remove light gray backgrounds from sketch images.
Works for black/white sketches on light backgrounds.
"""

import os
import glob
from PIL import Image
import numpy as np

# Configuration
INPUT_DIR = "images/chapterImages_optimized"
OUTPUT_DIR = "images/chapterImages_final"

# Threshold for background removal (adjust if needed)
# Pixels brighter than this will become transparent
BACKGROUND_THRESHOLD = 240  # 0-255, higher = more aggressive removal

def setup_directories():
    """Create output directory"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Output directory: {OUTPUT_DIR}")

def remove_light_background(input_path, output_path, threshold=BACKGROUND_THRESHOLD):
    """
    Remove light background from image.
    Converts light pixels to transparent.
    """
    try:
        # Open image
        img = Image.open(input_path).convert('RGBA')

        # Convert to numpy array
        data = np.array(img)

        # Get RGB channels
        r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]

        # Calculate brightness (average of RGB)
        brightness = (r.astype(float) + g.astype(float) + b.astype(float)) / 3

        # Create alpha channel: transparent where brightness > threshold
        # Fade out gradually near threshold for anti-aliasing
        fade_range = 20  # pixels near threshold will be semi-transparent
        alpha = np.zeros_like(brightness)

        # Fully opaque where dark enough
        alpha[brightness < threshold - fade_range] = 255

        # Gradually fade in the transition zone
        transition = (brightness >= threshold - fade_range) & (brightness <= threshold)
        fade_values = 255 * (threshold - brightness[transition]) / fade_range
        alpha[transition] = fade_values

        # Apply new alpha channel
        data[:,:,3] = alpha.astype(np.uint8)

        # Convert back to image
        result = Image.fromarray(data, 'RGBA')

        # Save
        result.save(output_path, 'PNG', optimize=True)

        return True
    except Exception as e:
        print(f"    Error: {e}")
        return False

def get_file_size_mb(filepath):
    """Get file size in MB"""
    return os.path.getsize(filepath) / (1024 * 1024)

def process_image(input_path):
    """Process a single image"""
    filename = os.path.basename(input_path)
    output_path = os.path.join(OUTPUT_DIR, filename)

    print(f"\n  {filename}")

    original_size = get_file_size_mb(input_path)
    print(f"    Original: {original_size:.2f} MB")

    if remove_light_background(input_path, output_path):
        final_size = get_file_size_mb(output_path)
        print(f"    With transparency: {final_size:.2f} MB")
        if final_size > original_size:
            print(f"    Note: Slightly larger due to alpha channel")
        return True

    return False

def main():
    """Main function"""
    print("="*70)
    print("Background Removal for The Genesis Code")
    print("="*70)
    print(f"Threshold: {BACKGROUND_THRESHOLD} (pixels brighter become transparent)")
    print()

    # Setup
    setup_directories()

    # Get images
    image_files = sorted(glob.glob(f"{INPUT_DIR}/*.png"))
    print(f"\nFound {len(image_files)} images")

    if not image_files:
        print("No images found!")
        print(f"Make sure images exist in: {INPUT_DIR}/")
        return

    # Process each image
    print("\nProcessing...")
    print("="*70)

    success_count = 0
    for image_path in image_files:
        if process_image(image_path):
            success_count += 1

    # Summary
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    print(f"Successfully processed: {success_count}/{len(image_files)} images")
    print(f"\nImages saved to: {OUTPUT_DIR}/")
    print("\nNext steps:")
    print("1. Review images to check background removal")
    print("2. Adjust BACKGROUND_THRESHOLD in script if needed (current: {})".format(BACKGROUND_THRESHOLD))
    print("3. If satisfied, update LaTeX paths to use new images")

if __name__ == "__main__":
    main()
