"""
Demo script for the Image Detection System
Creates a sample image and runs detection on it
"""

import os
from PIL import Image, ImageDraw
from image_detector import ImageDetector


def create_sample_image():
    """Create a sample image for testing."""
    sample_path = "example.jpg"
    
    if os.path.exists(sample_path):
        print(f"Using existing sample image: {sample_path}")
        return sample_path
    
    print("Creating sample test image...")
    try:
        # Create a simple test image with a cat-like drawing
        img = Image.new('RGB', (224, 224), color=(255, 250, 240))
        draw = ImageDraw.Draw(img)

        # Draw a simple cat face
        # Head (circle)
        draw.ellipse([50, 50, 174, 174], fill=(200, 200, 200), outline=(100, 100, 100), width=3)

        # Eyes
        draw.ellipse([80, 90, 100, 110], fill=(50, 50, 50))
        draw.ellipse([124, 90, 144, 110], fill=(50, 50, 50))

        # Pupils
        draw.ellipse([88, 96, 92, 104], fill=(255, 255, 255))
        draw.ellipse([132, 96, 136, 104], fill=(255, 255, 255))

        # Nose
        draw.polygon([(112, 120), (108, 130), (116, 130)], fill=(255, 150, 150))

        # Mouth
        draw.arc([90, 125, 134, 145], start=0, end=180, fill=(100, 100, 100), width=2)

        # Ears (triangles)
        draw.polygon([(60, 60), (50, 30), (80, 50)], fill=(200, 200, 200), outline=(100, 100, 100))
        draw.polygon([(164, 60), (174, 30), (144, 50)], fill=(200, 200, 200), outline=(100, 100, 100))

        # Whiskers
        draw.line([(50, 110), (30, 105)], fill=(100, 100, 100), width=2)
        draw.line([(50, 120), (30, 120)], fill=(100, 100, 100), width=2)
        draw.line([(174, 110), (194, 105)], fill=(100, 100, 100), width=2)
        draw.line([(174, 120), (194, 120)], fill=(100, 100, 100), width=2)

        img.save(sample_path, 'JPEG')
        print(f"Sample image created: {sample_path}")
        return sample_path
    except Exception as e:
        print(f"Failed to create sample image: {e}")
        return None


def main():
    """Run the demo."""
    print("=" * 60)
    print("Image Detection System - Demo")
    print("=" * 60)
    
    # Create sample image
    image_path = create_sample_image()
    
    if image_path is None:
        print("Error: Could not get sample image.")
        return
    
    # Create detector and run detection
    detector = ImageDetector()
    detector.detect_and_display(image_path, top_n=5)
    
    print("\n" + "=" * 60)
    print("Demo completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
