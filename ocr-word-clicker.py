import pyautogui
import pytesseract
import cv2
import os
import time
from datetime import datetime

# Path to Tesseract OCR (Specify the correct path for your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\Path\to\tesseract.exe'

def animated_dots(message, duration=3):
    """
    Displays a message with an animated dot effect.
    :param message: The message to display.
    :param duration: Duration of the animation (in seconds).
    """
    for _ in range(duration):
        for dots in range(4):  # Increase the number of dots
            print(f"\r{message}{'.' * dots}   ", end="", flush=True)
            time.sleep(0.5)
    print("\r", end="", flush=True)  # Clear the line

def find_and_click_text(target_text, interval=5):
    """
    Finds the specified word in a screenshot and clicks on it.
    Search and click outputs are formatted.
    :param target_text: The word to search for.
    :param interval: Time interval between searches (in seconds).
    """
    try:
        while True:
            # Start the search with an animated dot effect
            animated_dots(f"Searching for '{target_text}'")

            # Take a screenshot
            screenshot_path = os.path.abspath("screenshot.png")
            pyautogui.screenshot(screenshot_path)

            # Load the image using OpenCV
            img = cv2.imread(screenshot_path)
            if img is None:
                print("\nError: Could not load the image!")
                time.sleep(interval)
                continue

            # Use OCR to detect text
            text_data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)

            found = False
            for i, word in enumerate(text_data['text']):
                if word and target_text.lower() in word.lower():  # Case-insensitive matching
                    x, y, w, h = text_data['left'][i], text_data['top'][i], text_data['width'][i], text_data['height'][i]

                    # Perform the click action
                    pyautogui.click(x + w / 2, y + h / 2)

                    # Print a checkmark and timestamp when the word is found
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"\r✔ '{target_text}' found and clicked! [{current_time}]\n")

                    found = True
                    break

            if not found:
                # Restart animation for the next search
                print(f"'{target_text}' not found. Retrying in {interval} seconds...")
            time.sleep(interval)

    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
    except Exception as e:
        print(f"\nError occurred: {e}")

# Prompt user for the word to search
if __name__ == "__main__":
    target_text = input("Please enter the word to search for: ").strip()
    if target_text:
        find_and_click_text(target_text, interval=5)
    else:
        print("Invalid input. Program exiting.")
