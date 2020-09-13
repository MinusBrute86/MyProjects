import random
from tkinter import *
import tkinter as gui

# Creates GUI Window / MUST BE INCLUDED!
box = gui.Tk()

# Allows you to easily track tkinter variables and see if they have been read, overwritten, or if they even exist
rand_num = StringVar(box, value=random.randint(1, 3))

# setting the windows size
box.geometry("300x50")

# Creates Title for GUI
box.title('Random Number Generator')

# Creates Label within Gui
L1 = Label(box, text="Random Number:")
L1.grid(row=0, column=1)

# Creates Entry Field in GUI
E1 = Entry(box, bd=3, textvariable=rand_num)
E1.grid(row=0, column=3)


# Defining function to generate a new number when Button is clicked
def new_number():
    rand_num.set(random.randint(1, 3))


# Creates Button in GUI
B1 = Button(box, text='Generate', command=new_number)
B1.grid(row=2, column=2)

# Keeps GUI open till you close it / MUST BE INCLUDED!
box.mainloop()
