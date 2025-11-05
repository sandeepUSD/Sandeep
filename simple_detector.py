"""
Simple Image Detection System
Demonstrates image analysis and color/object detection without requiring pre-trained models
"""

import os
import sys
import numpy as np
from PIL import Image, ImageStat
from collections import Counter


class SimpleImageDetector:
    """
    A simple image detection system that analyzes image properties.
    Detects dominant colors, brightness, and basic shapes.
    """
    
    def __init__(self):
        """Initialize the simple image detector."""
        print("Simple Image Detector initialized!")
    
    def load_image(self, image_path):
        """
        Load an image from file.
        
        Args:
            image_path (str): Path to the image file
            
        Returns:
            PIL.Image: Loaded image
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found: {image_path}")
        
        return Image.open(image_path).convert('RGB')
    
    def get_dominant_colors(self, image, n_colors=5):
        """
        Extract the dominant colors from an image.
        
        Args:
            image (PIL.Image): Image to analyze
            n_colors (int): Number of dominant colors to return
            
        Returns:
            list: List of tuples (color_rgb, percentage)
        """
        # Resize for faster processing
        small_image = image.resize((150, 150))
        pixels = list(small_image.getdata())
        
        # Count color frequencies
        color_counts = Counter(pixels)
        total_pixels = len(pixels)
        
        # Get top N colors
        most_common = color_counts.most_common(n_colors)
        
        results = []
        for color, count in most_common:
            percentage = (count / total_pixels) * 100
            results.append((color, percentage))
        
        return results
    
    def get_color_name(self, rgb):
        """
        Get a human-readable color name from RGB values.
        
        Args:
            rgb (tuple): RGB color tuple
            
        Returns:
            str: Color name
        """
        r, g, b = rgb
        
        # Simple color naming based on dominant channel
        if r > 200 and g > 200 and b > 200:
            return "White/Light"
        elif r < 50 and g < 50 and b < 50:
            return "Black/Dark"
        elif r > 150 and g < 100 and b < 100:
            return "Red"
        elif r < 100 and g > 150 and b < 100:
            return "Green"
        elif r < 100 and g < 100 and b > 150:
            return "Blue"
        elif r > 150 and g > 150 and b < 100:
            return "Yellow"
        elif r > 150 and g < 100 and b > 150:
            return "Magenta"
        elif r < 100 and g > 150 and b > 150:
            return "Cyan"
        elif r > 100 and g > 100 and b > 100:
            return "Gray"
        elif r > 150 and g > 100 and b < 100:
            return "Orange/Brown"
        else:
            return "Mixed"
    
    def get_brightness(self, image):
        """
        Calculate average brightness of the image.
        
        Args:
            image (PIL.Image): Image to analyze
            
        Returns:
            float: Brightness value (0-255)
        """
        stat = ImageStat.Stat(image)
        # Average of R, G, B
        return sum(stat.mean) / 3
    
    def detect_edges(self, image):
        """
        Simple edge detection to estimate complexity.
        
        Args:
            image (PIL.Image): Image to analyze
            
        Returns:
            float: Edge density (0-1)
        """
        # Convert to grayscale
        gray = image.convert('L')
        pixels = np.array(gray)
        
        # Simple edge detection using gradient
        dx = np.diff(pixels, axis=1)
        dy = np.diff(pixels, axis=0)
        
        # Calculate edge density
        edge_pixels = (np.abs(dx) > 30).sum() + (np.abs(dy) > 30).sum()
        total_pixels = pixels.size
        
        return edge_pixels / total_pixels
    
    def analyze_image(self, image_path):
        """
        Perform comprehensive analysis of an image.
        
        Args:
            image_path (str): Path to the image file
            
        Returns:
            dict: Analysis results
        """
        image = self.load_image(image_path)
        
        # Get image properties
        width, height = image.size
        
        # Analyze colors
        dominant_colors = self.get_dominant_colors(image)
        
        # Get brightness
        brightness = self.get_brightness(image)
        
        # Detect edges/complexity
        edge_density = self.detect_edges(image)
        
        return {
            'dimensions': (width, height),
            'dominant_colors': dominant_colors,
            'brightness': brightness,
            'edge_density': edge_density,
            'format': image.format or 'Unknown'
        }
    
    def detect_and_display(self, image_path):
        """
        Detect properties in an image and display results.
        
        Args:
            image_path (str): Path to the image file
        """
        print(f"\nAnalyzing image: {image_path}")
        print("-" * 60)
        
        try:
            results = self.analyze_image(image_path)
            
            print(f"\nImage Properties:")
            print(f"  Dimensions: {results['dimensions'][0]}x{results['dimensions'][1]} pixels")
            print(f"  Brightness: {results['brightness']:.1f}/255")
            
            # Classify brightness
            if results['brightness'] > 200:
                brightness_class = "Very Bright"
            elif results['brightness'] > 150:
                brightness_class = "Bright"
            elif results['brightness'] > 100:
                brightness_class = "Moderate"
            elif results['brightness'] > 50:
                brightness_class = "Dim"
            else:
                brightness_class = "Very Dark"
            print(f"  Brightness Level: {brightness_class}")
            
            # Edge density / complexity
            complexity = "High" if results['edge_density'] > 0.3 else "Moderate" if results['edge_density'] > 0.15 else "Low"
            print(f"  Image Complexity: {complexity}")
            
            print(f"\nDominant Colors:")
            for i, (color, percentage) in enumerate(results['dominant_colors'], 1):
                color_name = self.get_color_name(color)
                print(f"  {i}. {color_name} RGB{color}: {percentage:.2f}%")
            
            print("-" * 60)
            
        except Exception as e:
            print(f"Error processing image: {str(e)}")
            raise


def main():
    """Main function to demonstrate the image detector."""
    if len(sys.argv) < 2:
        print("Usage: python simple_detector.py <image_path>")
        print("Example: python simple_detector.py example.jpg")
        sys.exit(1)
    
    image_path = sys.argv[1]
    
    # Create detector instance
    detector = SimpleImageDetector()
    
    # Detect and display results
    detector.detect_and_display(image_path)


if __name__ == "__main__":
    main()
