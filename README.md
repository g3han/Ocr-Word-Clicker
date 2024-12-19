# OCR Word Clicker

This Python project captures screenshots of your screen, uses OCR (Optical Character Recognition) to find a specified word, and clicks on the word's location. The program runs continuously until you manually stop it.

## Features
- Continuously searches for a specific word on the screen.
- Uses OCR to detect the word and clicks on its position.
- Simple to configure and run.
- Logs actions and handles errors gracefully.

## Requirements

### Software Prerequisites
- **Python 3.8 or higher**: Ensure Python is installed on your system.
- **Tesseract OCR**:
  - Download and install Tesseract OCR from [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract).
  - During installation, ensure the `tessdata` folder and `tesseract.exe` are accessible.

### Python Libraries
Install the following Python libraries using `pip`:
```bash
pip install pyautogui pytesseract opencv-python
```

## Setup Instructions

1. **Clone or Download the Repository**
   Download the project from GitHub or clone it using:
   ```bash
   git clone https://github.com/yourusername/ocr-word-clicker.git
   cd ocr-word-clicker
   ```

2. **Verify Tesseract Installation**
   Ensure Tesseract OCR is installed and its path is correctly set in the script:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

   Update the path if Tesseract is installed in a different location.

3. **Run the Script**
   Execute the Python script:
   ```bash
   python wordclicker.py
   ```

4. **Enter the Target Word**
   When prompted, input the word you want the program to find and click on.

## How It Works

1. The program takes a screenshot of your entire screen using PyAutoGUI.
2. The screenshot is processed using Tesseract OCR to extract text.
3. If the specified word is found, the program calculates its position and clicks on it.
4. The program runs in a continuous loop, searching and clicking until stopped.

## Customization

### Change Search Interval
You can adjust the interval between searches by modifying the `interval` parameter in the script:
```python
find_and_click_text(target_text, interval=5)
```

### Support for Multiple Words
To search for multiple words, replace `target_text` with a list and update the logic to iterate over the list.

### Add Logging
To log actions to a file, add a logging mechanism to the script:
```python
import logging
logging.basicConfig(filename='wordclicker.log', level=logging.INFO)
```

### Change OCR Language
If you want to use OCR for a different language (e.g., Turkish), modify the language parameter in the script:
```python
text_data = pytesseract.image_to_data(img, lang='tur', output_type=pytesseract.Output.DICT)
```

## Stopping the Program
The program runs continuously. To stop it, press `Ctrl + C` in the terminal.

## Troubleshooting

### Common Errors

1. **`Error opening data file ./eng.traineddata`**:
   - Ensure Tesseract is installed correctly and the `TESSDATA_PREFIX` environment variable points to the `tessdata` directory.

2. **`No module named 'pyautogui'`**:
   - Install the missing library using `pip install pyautogui`.

3. **Click Issues**:
   - Ensure the resolution of your screen matches the resolution used during testing.

### Debugging Tips
- Use `print` statements or logging to debug OCR outputs.
- Check if Tesseract is correctly identifying text by printing `text_data` to the console.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it.

## Contributing
Contributions are welcome! If you encounter issues or have suggestions, feel free to open an issue or submit a pull request.

