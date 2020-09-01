from yahoo_fin.stock_info import get_live_price
from tkinter import *
import tkinter as tk

running = False


def get_stock_price():
    if running:
        ticker_sym1 = get_live_price(str(E1.get()))
        print(str(ticker_sym1))
        E11.delete(0, END)
        E11.insert(0, str(ticker_sym1))

        ticker_sym1 = get_live_price(str(E2.get()))
        print(str(ticker_sym1))
        E12.delete(0, END)
        E12.insert(0, str(ticker_sym1))

        ticker_sym1 = get_live_price(str(E3.get()))
        print(str(ticker_sym1))
        E13.delete(0, END)
        E13.insert(0, str(ticker_sym1))

        ticker_sym1 = get_live_price(str(E4.get()))
        print(str(ticker_sym1))
        E14.delete(0, END)
        E14.insert(0, str(ticker_sym1))

        ticker_sym1 = get_live_price(str(E5.get()))
        print(str(ticker_sym1))
        E15.delete(0, END)
        E15.insert(0, str(ticker_sym1))
    gui.after(500, get_stock_price)


def start():
    global running
    running = True


def stop():
    global running
    running = False


def clear():
    print('Clear')
    E1.delete(0, END)
    E2.delete(0, END)
    E3.delete(0, END)
    E4.delete(0, END)
    E5.delete(0, END)
    E11.delete(0, END)
    E12.delete(0, END)
    E13.delete(0, END)
    E14.delete(0, END)
    E15.delete(0, END)

    global running
    running = False


# Creates GUI
gui = tk.Tk()
gui.title('Price Viewer')
gui.geometry('285x215')
gui.resizable(False, False)

# Creates Labels
L1 = Label(gui, text='Stock Price')
L2 = Label(gui, text='Stock Ticker')
L1.grid(row=0, column=2)
L2.grid(row=0, column=1)

# Creates Entries
E11 = Entry(gui, bd=3)
E12 = Entry(gui, bd=3)
E13 = Entry(gui, bd=3)
E14 = Entry(gui, bd=3)
E15 = Entry(gui, bd=3)

E11.grid(row=1, column=2)
E12.grid(row=2, column=2)
E13.grid(row=3, column=2)
E14.grid(row=4, column=2)
E15.grid(row=5, column=2)

# Entry for Input (Stock Ticker Input)
E1 = Entry(gui, bd=3)
E2 = Entry(gui, bd=3)
E3 = Entry(gui, bd=3)
E4 = Entry(gui, bd=3)
E5 = Entry(gui, bd=3)

E1.grid(row=1, column=1, padx=10, pady=1)
E2.grid(row=2, column=1, padx=10, pady=1)
E3.grid(row=3, column=1, padx=10, pady=1)
E4.grid(row=4, column=1, padx=10, pady=1)
E5.grid(row=5, column=1, padx=10, pady=1)

# Creates Buttons
B1 = Button(gui, text='Start', command=start)
B2 = Button(gui, text='Stop', command=stop)
B1.grid(row=6, column=1)
B2.grid(row=6, column=2)

# Clear All Entries
B3 = Button(gui, text='Clear All', command=clear)
B3.grid(row=7, column=1, columnspan=2)

# Keeps GUI running till closed
gui.after(1000, get_stock_price)
gui.mainloop()