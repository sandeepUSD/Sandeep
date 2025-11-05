# Image Detection System

A simple image detection system built with Python. Provides two implementations:
1. **Simple Detector**: Analyzes images for colors, brightness, and complexity (no network required)
2. **Advanced Detector**: Uses TensorFlow with pre-trained MobileNetV2 for object classification (requires network access)

## Features

### Simple Detector (Recommended for Getting Started)
- ✅ No network access required
- Dominant color detection with percentage analysis
- Brightness and complexity analysis
- Works with any image format (JPEG, PNG, etc.)
- Easy-to-use command-line interface
- Perfect first project for learning image processing

### Advanced Detector
- Object detection and classification using MobileNetV2 pre-trained on ImageNet
- Recognizes 1000+ object categories
- Returns top N predictions with confidence scores
- Requires internet connection for first-time model download

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sandeepUSD/Sandeep.git
cd Sandeep
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Quick Start with Simple Detector (Recommended)

Run the demo to see the system in action:

```bash
python simple_demo.py
```

This will create sample images and analyze them, showing:
- Image dimensions
- Brightness levels
- Dominant colors
- Image complexity

### Analyze Your Own Images

Use the simple detector on any image:

```bash
python simple_detector.py <path_to_your_image>
```

Example:
```bash
python simple_detector.py my_photo.jpg
```

### Advanced Detection (Requires Network)

For object classification with pre-trained models:

```bash
python demo.py                      # Run demo with TensorFlow
python image_detector.py my_photo.jpg  # Analyze specific image
```

### Use as a Python Module

Simple detector:
```python
from simple_detector import SimpleImageDetector

# Create detector instance
detector = SimpleImageDetector()

# Analyze an image
results = detector.analyze_image("path/to/image.jpg")

# Display results
detector.detect_and_display("path/to/image.jpg")
```

Advanced detector:
```python
from image_detector import ImageDetector

# Create detector instance
detector = ImageDetector()

# Detect objects in an image
predictions = detector.detect("path/to/image.jpg", top_n=5)

# Display results
for class_id, class_name, probability in predictions:
    print(f"{class_name}: {probability*100:.2f}%")
```

## How It Works

### Simple Detector
1. **Color Analysis**: Extracts dominant colors and calculates their percentages
2. **Brightness**: Computes average brightness across RGB channels
3. **Edge Detection**: Estimates image complexity using gradient analysis
4. **Classification**: Provides human-readable color names and brightness levels

### Advanced Detector
1. **Model**: Uses MobileNetV2, a lightweight convolutional neural network pre-trained on ImageNet
2. **Preprocessing**: Images are resized to 224x224 pixels and normalized
3. **Detection**: The model predicts the most likely object categories
4. **Results**: Returns top N predictions with confidence scores

## Requirements

- Python 3.7+
- TensorFlow 2.12.1+
- NumPy 1.23+
- Pillow 10.2+

## Project Structure

```
Sandeep/
├── simple_detector.py   # Simple detection module (no network needed)
├── simple_demo.py       # Demo for simple detector
├── image_detector.py    # Advanced TensorFlow detection module
├── demo.py             # Demo for TensorFlow detector
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Example Output

### Simple Detector
```
Analyzing image: example_colors.jpg
------------------------------------------------------------

Image Properties:
  Dimensions: 224x224 pixels
  Brightness: 129.6/255
  Brightness Level: Moderate
  Image Complexity: Low

Dominant Colors:
  1. Gray RGB(128, 128, 128): 13.68%
  2. Yellow RGB(255, 165, 0): 12.00%
  3. Blue RGB(0, 0, 254): 8.40%
  4. Red RGB(254, 0, 0): 8.32%
  5. Cyan RGB(0, 255, 255): 8.23%
------------------------------------------------------------
```

### Advanced Detector
Recognizes 1000+ categories from ImageNet, including:
- Animals (dogs, cats, birds, etc.)
- Vehicles (cars, bikes, planes, etc.)
- Household items (furniture, appliances, etc.)
- Food items
- And many more!

## Getting Started as Your First Project

This project is perfect as a first project because:
1. **Simple Detector** requires no external APIs or model downloads
2. Clear, well-commented code that's easy to understand
3. Demonstrates fundamental image processing concepts
4. Can be extended with your own detection algorithms
5. Provides both simple and advanced implementations for learning

Start with `simple_demo.py` to see it in action, then explore the code to understand how it works!

## License

This project is open source and available for educational purposes.

## Author

Sandeep