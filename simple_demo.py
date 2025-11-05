"""
Demo script for the Simple Image Detection System
Creates sample images and runs detection on them
"""

import os
from PIL import Image, ImageDraw
from simple_detector import SimpleImageDetector


def create_test_images():
    """Create multiple test images for demonstration."""
    test_images = []
    
    # Test Image 1: Cat face
    if not os.path.exists("example_cat.jpg"):
        print("Creating cat face test image...")
        img = Image.new('RGB', (224, 224), color=(255, 250, 240))
        draw = ImageDraw.Draw(img)
        
        # Draw a simple cat face
        draw.ellipse([50, 50, 174, 174], fill=(200, 200, 200), outline=(100, 100, 100), width=3)
        draw.ellipse([80, 90, 100, 110], fill=(50, 50, 50))
        draw.ellipse([124, 90, 144, 110], fill=(50, 50, 50))
        draw.ellipse([88, 96, 92, 104], fill=(255, 255, 255))
        draw.ellipse([132, 96, 136, 104], fill=(255, 255, 255))
        draw.polygon([(112, 120), (108, 130), (116, 130)], fill=(255, 150, 150))
        draw.arc([90, 125, 134, 145], start=0, end=180, fill=(100, 100, 100), width=2)
        draw.polygon([(60, 60), (50, 30), (80, 50)], fill=(200, 200, 200), outline=(100, 100, 100))
        draw.polygon([(164, 60), (174, 30), (144, 50)], fill=(200, 200, 200), outline=(100, 100, 100))
        draw.line([(50, 110), (30, 105)], fill=(100, 100, 100), width=2)
        draw.line([(50, 120), (30, 120)], fill=(100, 100, 100), width=2)
        draw.line([(174, 110), (194, 105)], fill=(100, 100, 100), width=2)
        draw.line([(174, 120), (194, 120)], fill=(100, 100, 100), width=2)
        
        img.save("example_cat.jpg", 'JPEG')
        print("  Created: example_cat.jpg")
    test_images.append("example_cat.jpg")
    
    # Test Image 2: Colorful pattern
    if not os.path.exists("example_colors.jpg"):
        print("Creating colorful pattern test image...")
        img = Image.new('RGB', (224, 224), color=(255, 255, 255))
        draw = ImageDraw.Draw(img)
        
        # Draw colorful rectangles
        draw.rectangle([0, 0, 74, 74], fill=(255, 0, 0))  # Red
        draw.rectangle([75, 0, 149, 74], fill=(0, 255, 0))  # Green
        draw.rectangle([150, 0, 224, 74], fill=(0, 0, 255))  # Blue
        draw.rectangle([0, 75, 74, 149], fill=(255, 255, 0))  # Yellow
        draw.rectangle([75, 75, 149, 149], fill=(255, 0, 255))  # Magenta
        draw.rectangle([150, 75, 224, 149], fill=(0, 255, 255))  # Cyan
        draw.rectangle([0, 150, 112, 224], fill=(128, 128, 128))  # Gray
        draw.rectangle([113, 150, 224, 224], fill=(255, 165, 0))  # Orange
        
        img.save("example_colors.jpg", 'JPEG')
        print("  Created: example_colors.jpg")
    test_images.append("example_colors.jpg")
    
    # Test Image 3: Simple shapes
    if not os.path.exists("example_shapes.jpg"):
        print("Creating shapes test image...")
        img = Image.new('RGB', (224, 224), color=(220, 240, 255))
        draw = ImageDraw.Draw(img)
        
        # Draw various shapes
        draw.ellipse([20, 20, 100, 100], fill=(0, 150, 200), outline=(0, 100, 150), width=3)
        draw.rectangle([120, 20, 200, 100], fill=(200, 100, 0), outline=(150, 50, 0), width=3)
        draw.polygon([(60, 120), (20, 200), (100, 200)], fill=(100, 200, 100), outline=(50, 150, 50))
        draw.polygon([(162, 120), (122, 160), (142, 210), (182, 210), (202, 160)], 
                     fill=(200, 100, 200), outline=(150, 50, 150))
        
        img.save("example_shapes.jpg", 'JPEG')
        print("  Created: example_shapes.jpg")
    test_images.append("example_shapes.jpg")
    
    return test_images


def main():
    """Run the demo."""
    print("=" * 60)
    print("Simple Image Detection System - Demo")
    print("=" * 60)
    print()
    
    # Create test images
    test_images = create_test_images()
    print()
    
    # Create detector
    detector = SimpleImageDetector()
    print()
    
    # Analyze each test image
    for image_path in test_images:
        detector.detect_and_display(image_path)
        print()
    
    print("=" * 60)
    print("Demo completed successfully!")
    print("=" * 60)
    print()
    print(f"Test images created: {', '.join(test_images)}")
    print("You can analyze your own images using:")
    print("  python simple_detector.py <your_image.jpg>")


if __name__ == "__main__":
    main()
