# webp-to-jpg
This Python script converts all .webp images in a specified folder to .jpg format. The converted files are saved in a designated output folder.

## Features
- Converts .webp images to .jpg format.
- Automatically creates the output directory if it doesn’t exist.
- Maintains high image quality during conversion.

## Requirements
- Python 3.6 or higher
- Pillow library

## Installation
1. Clone this repository or download the script:

```bash
git clone https://github.com/pongsapak-suwa/webp-to-jpg.git
cd webp-to-jpg
```

2. Install the required Python library:
```bash
pip install pillow
```

## Usage
1. Update the script with your desired input and output folder paths:
```python
input_folder = r"D:\\Path\\To\\Input\\Folder"
output_folder = r"D:\\Path\\To\\Output\\Folder"
```

2. Run the script:
```bash
python main.py
The converted .jpg images will appear in the specified output folder.
```

## Example
Input folder structure:

```mathematica

D:\\Path\\To\\Input\\Folder\
    image1.webp
    image2.webp
```
Output folder structure after running the script:

```mathematica

D:\\Path\\To\\Output\\Folder\\
    image1.jpg
    image2.jpg
```

---
