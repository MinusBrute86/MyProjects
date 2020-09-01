from tkinter import *
import tkinter as tk
# ---------------------------------------------------------------------------------------------------------------------

# Creates GUI
gui = tk.Tk()
gui.geometry("225x300")
gui.title("My First Calculator")
# ---------------------------------------------------------------------------------------------------------------------

# Defining Variables
number = StringVar()
# ---------------------------------------------------------------------------------------------------------------------

# Creates Entry Field
E1 = Entry(gui, bd=3, width=30, textvariable=number)
E1.grid(row=0, column=0, columnspan=4, padx=15, pady=15)
# ---------------------------------------------------------------------------------------------------------------------
# Defines Method/Function to import number to entry Field to corresponding Button clicked


def clicked(number):
    current = E1.get()
    E1.delete(0, END)
    E1.insert(0, str(current) + str(number))
# ---------------------------------------------------------------------------------------------------------------------


# Defines Method/Function for clearing Entry Field
def clear():
    print("C")
    E1.delete(0, END)
# ---------------------------------------------------------------------------------------------------------------------


# Creates Number Buttons
B1 = Button(gui, text="1", command=lambda:clicked(1), padx=15, pady=15)
B2 = Button(gui, text="2", command=lambda:clicked(2), padx=15, pady=15)
B3 = Button(gui, text="3", command=lambda:clicked(3), padx=15, pady=15)
B4 = Button(gui, text="4", command=lambda:clicked(4), padx=15, pady=15)
B5 = Button(gui, text="5", command=lambda:clicked(5), padx=15, pady=15)
B6 = Button(gui, text="6", command=lambda:clicked(6), padx=15, pady=15)
B7 = Button(gui, text="7", command=lambda:clicked(7), padx=15, pady=15)
B8 = Button(gui, text="8", command=lambda:clicked(8), padx=15, pady=15)
B9 = Button(gui, text="9", command=lambda:clicked(9), padx=15, pady=15)
B10 = Button(gui, text="0", command=lambda:clicked(0), padx=15, pady=15)

# Places Buttons in the GUI
B1.grid(row=3, column=0)
B2.grid(row=3, column=1)
B3.grid(row=3, column=2)
B4.grid(row=2, column=0)
B5.grid(row=2, column=1)
B6.grid(row=2, column=2)
B7.grid(row=1, column=0)
B8.grid(row=1, column=1)
B9.grid(row=1, column=2)
B10.grid(row=4, column=1)

# Creates/ Places Clear Button
BC = Button(gui, text="C", command=clear, padx=14, pady=15)
BC.grid(row=4, column=0)
# ---------------------------------------------------------------------------------------------------------------------

# Defines Method/Function for Math Equations


def addition():
    print("+")
    global f_num
    global math
    math = "add"
    first_num = E1.get()
    f_num = int(first_num)
    E1.delete(0, END)


def subtraction():
    print("-")
    global f_num
    global math
    math = "subtract"
    first_num = E1.get()
    f_num = int(first_num)
    E1.delete(0, END)


def multiplication():
    print("x")
    global f_num
    global math
    math = "multiply"
    first_num = E1.get()
    f_num = int(first_num)
    E1.delete(0, END)


def division():
    print("/")
    global f_num
    global math
    math = "divide"
    first_num = E1.get()
    f_num = int(first_num)
    E1.delete(0, END)
# ---------------------------------------------------------------------------------------------------------------------

# Outputs desired value after corresponding equation


def value():
    print("=")
    global f_num2

    if math == "add":
        second_num = E1.get()
        f_num2 = int(second_num)
        E1.delete(0, END)
        E1.insert(0, f_num + f_num2)

    if math == "subtract":
        second_num = E1.get()
        f_num2 = int(second_num)
        E1.delete(0, END)
        E1.insert(0, f_num - f_num2)

    if math == "multiply":
        second_num = E1.get()
        f_num2 = int(second_num)
        E1.delete(0, END)
        E1.insert(0, f_num * f_num2)

    if math == "divide":
        second_num = E1.get()
        f_num2 = int(second_num)
        E1.delete(0, END)
        E1.insert(0, f_num / f_num2)
# ---------------------------------------------------------------------------------------------------------------------


# Creates Function Buttons
BA = Button(gui, text="+", command=addition, padx=14, pady=15)
BS = Button(gui, text="-", command=subtraction, padx=15, pady=15)
BM = Button(gui, text="x", command=multiplication, padx=14, pady=15)
BD = Button(gui, text="/", command=division, padx=15, pady=15)
BE = Button(gui, text="=", padx=14, pady=15, command=value)

# Places Buttons in the GUI
BA.grid(row=1, column=3)
BS.grid(row=2, column=3)
BM.grid(row=3, column=3)
BD.grid(row=4, column=3)
BE.grid(row=4, column=2)
# ---------------------------------------------------------------------------------------------------------------------

# Keeps GUI running till closed
gui.mainloop()