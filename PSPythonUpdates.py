import os
import pyautogui
import time


def open_file():
    os.startfile(r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe')
    time.sleep(1)
    pyautogui.write('pip freeze | %{$_.split("==")[0]} | %{pip install --upgrade $_}')
    time.sleep(1)
    pyautogui.press('return')


open_file()