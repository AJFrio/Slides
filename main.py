import pyautogui
import time

def makeSong(songName):
    # Add safety delay and failsafe
    pyautogui.FAILSAFE = True
    time.sleep(2)  # Initial delay before starting

    # Read lines from the file
    with open(f'songs/{songName}.txt', 'r') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]  # Remove trailing whitespace/newlines

    for i in range(0, len(lines), 2):
        #layout
        pyautogui.click(1107, 291)
        time.sleep(0.5)

        #Title
        pyautogui.click(1135, 360)
        time.sleep(0.5)
        pyautogui.click(1085, 674)
        # Type two lines
        pyautogui.write(lines[i] + "\n")
        if i + 1 < len(lines):  # Check if there's a second line
            pyautogui.write(lines[i + 1] + "\n")
        time.sleep(0.5)
        
        # Click the position (except after the last group)
        if i + 2 < len(lines):
            pyautogui.click(115, 281)
            time.sleep(0.5)  # Small delay between groups
        
        
makeSong("four")