import datetime
import os
import time
import pyautogui

# Directory to save screenshots
SAVE_DIR = 'screenshots'
os.makedirs(SAVE_DIR, exist_ok=True)

def capture_screenshots():
    """Captures screenshots at regular intervals and saves them to the specified directory."""
    while True:
        # Capture Screenshot
        screenshot = pyautogui.screenshot()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        image_path = os.path.join(SAVE_DIR, f"screenshot_{timestamp}.png")
        screenshot.save(image_path)
        print(f"Screenshot saved: {image_path}")
        
        # Wait before capturing the next screenshot
        time.sleep(30)

if __name__ == "__main__":
    capture_screenshots()
