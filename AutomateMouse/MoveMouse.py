import pyautogui
import time

print(pyautogui.size())

while True:
    pyautogui.moveTo(350,450, duration=2)
    time.sleep(5)
    pyautogui.moveTo(960,540, duration=2)
    time.sleep(5)