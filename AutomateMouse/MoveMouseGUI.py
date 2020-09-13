import pyautogui
import tkinter as tk
from tkinter import *
import time

# Create GUI/Title/Size
gui = tk.Tk()
gui.title('Automated Mouse')
gui.geometry('300x250')
gui.resizable(False, False)

# Print Monitor Size to Label
Spec_Label = Label(gui, text='Your Monitor Size:').grid(row=5, column=0, columnspan=2)
Size_Label = Label(gui, text=pyautogui.size()).grid(row=6, column=0, columnspan=2)
Desc_Label = Label(gui, text='**(Max-Width^^ | ^^Max-Height)**').grid(row=7, column=0, columnspan=2)

# Labels for Minimums
L1 = Label(gui, text='1st Width (x):').grid(row=0, column=0, padx=10, pady=10)
L2 = Label(gui, text='1st Height (y):').grid(row=0, column=1, padx=10, pady=10)

# Labels for Maximums
L3 = Label(gui, text='2nd Width (x):').grid(row=2, column=0, pady=10)
L4 = Label(gui, text='2nd Height (y):').grid(row=2, column=1, pady=10)

# Move Mouse Around

running = False


def move():
    if running:
        pyautogui.moveTo(int(E1.get()), int(E2.get()), duration=2)
        time.sleep(2)
        pyautogui.moveTo(int(E3.get()), int(E4.get()), duration=2)
        time.sleep(2)
    gui.after(1000, move)


def start():
    global running
    running = True


def stop():
    global running
    running = False


# First (x, y) point where mouse starts
E1 = Entry(gui, bd=3)
E1.grid(row=1, column=0, padx=10)
E2 = Entry(gui, bd=3)
E2.grid(row=1, column=1, padx=10)

# Second (x, y) points where mouse ends
E3 = Entry(gui, bd=3)
E3.grid(row=3, column=0)
E4 = Entry(gui, bd=3)
E4.grid(row=3, column=1)

# Start & Stop Buttons
B1 = Button(gui, bd=3, text='Start', command=start).grid(row=4, column=0, pady=10)
B2 = Button(gui, bd=3, text='Stop', command=stop).grid(row=4, column=1, pady=10)

# Main loop to keep GUI running
gui.after(1000, move)
gui.mainloop()