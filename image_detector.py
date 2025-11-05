"""
Simple Image Detection System
Uses MobileNetV2 pre-trained on ImageNet for object detection/classification
"""

import os
import sys
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image


class ImageDetector:
    """
    A simple image detection system using pre-trained MobileNetV2 model.
    """
    
    def __init__(self):
        """Initialize the image detector with pre-trained model."""
        print("Loading MobileNetV2 model...")
        self.model = MobileNetV2(weights='imagenet')
        print("Model loaded successfully!")
    
    def load_and_preprocess_image(self, image_path, target_size=(224, 224)):
        """
        Load and preprocess an image for the model.
        
        Args:
            image_path (str): Path to the image file
            target_size (tuple): Target size for the image (default: 224x224)
            
        Returns:
            numpy.ndarray: Preprocessed image array
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found: {image_path}")
        
        # Load image
        img = image.load_img(image_path, target_size=target_size)
        
        # Convert to array
        img_array = image.img_to_array(img)
        
        # Add batch dimension
        img_array = np.expand_dims(img_array, axis=0)
        
        # Preprocess for MobileNetV2
        img_array = preprocess_input(img_array)
        
        return img_array
    
    def detect(self, image_path, top_n=5):
        """
        Detect objects in an image.
        
        Args:
            image_path (str): Path to the image file
            top_n (int): Number of top predictions to return (default: 5)
            
        Returns:
            list: List of tuples (class_id, class_name, probability)
        """
        # Load and preprocess image
        processed_image = self.load_and_preprocess_image(image_path)
        
        # Make prediction
        predictions = self.model.predict(processed_image, verbose=0)
        
        # Decode predictions
        decoded_predictions = decode_predictions(predictions, top=top_n)[0]
        
        return decoded_predictions
    
    def detect_and_display(self, image_path, top_n=5):
        """
        Detect objects in an image and display results.
        
        Args:
            image_path (str): Path to the image file
            top_n (int): Number of top predictions to return (default: 5)
        """
        print(f"\nAnalyzing image: {image_path}")
        print("-" * 60)
        
        try:
            predictions = self.detect(image_path, top_n)
            
            print(f"\nTop {top_n} predictions:")
            for i, (class_id, class_name, probability) in enumerate(predictions, 1):
                print(f"{i}. {class_name.replace('_', ' ').title()}: {probability*100:.2f}%")
            
            print("-" * 60)
            
        except Exception as e:
            print(f"Error processing image: {str(e)}")
            raise


def main():
    """Main function to demonstrate the image detector."""
    if len(sys.argv) < 2:
        print("Usage: python image_detector.py <image_path>")
        print("Example: python image_detector.py example.jpg")
        sys.exit(1)
    
    image_path = sys.argv[1]
    
    # Create detector instance
    detector = ImageDetector()
    
    # Detect and display results
    detector.detect_and_display(image_path)


if __name__ == "__main__":
    main()
