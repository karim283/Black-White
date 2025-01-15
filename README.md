# Image Compare Tool

## Overview
The Image Compare Tool is a Python application built using Tkinter for the graphical user interface (GUI) and Pillow (PIL) for image processing. The tool allows users to:
- Upload an image.
- Convert it to black & white.
- Visually compare it with the original image.
- Highlight pixel differences between the two images.
- Count and display differing pixels.

## Features
- Upload an image through a file dialog.
- Convert the uploaded image to grayscale.
- Compare the original image and its black & white version.
- Visualize differences between the two images.
- Count and display differing pixels.
- Display results in a graphical interface.

## Technologies Used
- **Tkinter**: For the GUI.
- **Pillow (PIL)**: For image manipulation.
- **NumPy**: For efficient array manipulation.
- **Matplotlib**: For displaying images.
- **Python 3.x**: Programming language.

## Installation

### Prerequisites
- Python 3.
- Libraries:
  - Pillow
  - NumPy
  - Matplotlib
  - Tkinter (usually bundled with Python).

### Steps to Install
1. Clone or download the repository.
2. Install the required libraries:
   ```bash
   pip install pillow numpy matplotlib
   ```
3. Run the application:
   ```bash
   python image_compare_tool.py
   ```

## Usage

1. **Launch the application**: Run `image_compare_tool.py`.
2. **Upload an image**: Click the "Upload Image" button and select a file (JPG, PNG, BMP, etc.).
3. **Image processing**:
   - Converts the image to grayscale.
   - Compares original and grayscale images pixel by pixel.
   - Highlights differences visually.
4. **Results**:
   - View original, black & white, and difference heatmap.
   - A message box shows the total number of differing pixels.
5. **Exit the application**: Close the window.

## How It Works

### Image Conversion
1. Opens the image using Pillow.
2. Converts the image to grayscale.

### Image Comparison
1. Extracts pixel values using NumPy arrays.
2. Converts grayscale to 3-channel format if the original is colored.
3. Computes the absolute difference between pixels.
4. Counts differing pixels.

### Display Differences
1. Uses Matplotlib to plot three images:
   - Original image.
   - Grayscale image.
   - Heatmap of differences.

## Key Functions
- **`convert(path)`**: Opens and converts the image to grayscale.
- **`compares(original, blackwhite)`**: Computes pixel differences.
- **`show(original, blackwhite, diff)`**: Displays the images using Matplotlib.
- **`process(path)`**: Coordinates image conversion, comparison, and display.
- **`upload()`**: Handles file selection and triggers processing.

## Example

### Before:
A colorful image of a landscape.

### After:
- Converted to black & white.
- Differences shown in a heatmap.
- Total differing pixels displayed in a message box.

## Troubleshooting
- **Error Handling**: Displays error messages if processing fails.
- **Large Images**: Resize large images before uploading to avoid performance issues.
- **No File Selected**: If no file is selected, processing will not proceed.

## Contributing
1. Fork the repository.
2. Create a new branch.
3. Submit a pull request.
4. Ensure changes are documented and tested.

## License
This project is available under the MIT License.

