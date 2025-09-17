# 🖼️ Image Converter

A simple Python script to convert images into different formats using Pillow (PIL). The app supports both single-image conversion and bulk conversion of all images in a folder.

## 🚀 Features

- Converts images into popular formats: JPG, JPEG, PNG, GIF, BMP, TIFF, WEBP.
- Works with both single files and entire folders.
- Creates destination folders automatically if they don’t exist.
- Preserves the original filename when converting.
- Interactive command-line interface for ease of use.

### 🛠️ Requirements

•Python 3.8+

•Pillow library (install via pip):

    pip install pillow

### ▶️ Usage

Run the script:

    python app.py


Follow the prompts:

1. Choose between converting a single image or multiple images.

2. Enter the source path (file or folder).

3. Enter the desired output format (e.g., PNG, WEBP).

4. (Optional) Enter a destination folder. Leave empty to save in the original folder.

### 📈 Example output
    ===IMAGES CONVERTER ===
    Available formats:
    - JPG
    - JPEG
    - PNG
    - GIF
    - BMP
    - TIFF
    - WEBP
    
    Options:
    1. Convert a single image
    2. Convert multiple images within a folder
    
    Choose an option (1-2): 2
    Insert the path of the image you want to convert: ./photos
    Insert the format you want to convert the image to (ej: PNG): WEBP
    Insert the destination folder where you want to save the converted image (leave it empty to use the same folder as the original image):
    
    ✅ Image converted and saved in: ./photos/photo1.webp
    ✅ Image converted and saved in: ./photos/photo2.webp
    
    It converted 2 images successfully!

### 🧩 Functions Overview

• display_compatible_formats() → Prints supported formats.

• convert_image(image_path, output_format, destination_folder=None) → Converts a single image to the specified format.

• convert_multiple_images(origin_folder, output_format, destination_folder=None) → Converts all images in a folder.

• main() → Interactive CLI menu.

### 📜 License

This project is licensed under the MIT License.
