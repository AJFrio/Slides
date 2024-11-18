import pyautogui
import time

time.sleep(4)
x, y = pyautogui.position()
print(f'Cursor position: x={x}, y={y}')