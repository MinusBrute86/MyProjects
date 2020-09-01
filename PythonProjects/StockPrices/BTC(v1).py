from yahoo_fin.stock_info import get_live_price
from tkinter import *
import tkinter as tk

running = False


def get_stock_price():
    if running:
        ticker_sym1 = get_live_price('BTC-USD')
        print(str(ticker_sym1))
        E1.delete(0, END)
        E1.insert(0, str(ticker_sym1))

        ticker_sym2 = get_live_price('ETH-USD')
        print(str(ticker_sym2))
        E2.delete(0, END)
        E2.insert(0, str(ticker_sym2))

        ticker_sym3 = get_live_price('TSLA')
        print(str(ticker_sym3))
        E3.delete(0, END)
        E3.insert(0, str(ticker_sym3))
    gui.after(1000, get_stock_price)


def start():
    global running
    running = True


def stop():
    global running
    running = False


# Creates GUI
gui = tk.Tk()
gui.title('Price Viewer')
gui.geometry('250x125')

# Creates Labels
L1 = Label(gui, text='Stock Price')
L2 = Label(gui, text='BTC-USD:')
L3 = Label(gui, text='ETH-USD:')
L4 = Label(gui, text='TSLA:')
L1.grid(row=0, column=2)
L2.grid(row=1, column=0)
L3.grid(row=2, column=0)
L4.grid(row=3, column=0)

# Creates Entries
E1 = Entry(gui, bd=3)
E2 = Entry(gui, bd=3)
E3 = Entry(gui, bd=3)
E1.grid(row=1, column=2)
E2.grid(row=2, column=2)
E3.grid(row=3, column=2)

# Creates Buttons
B1 = Button(gui, text='Start', command=start)
B2 = Button(gui, text='Stop', command=stop)
B1.grid(row=4, column=0)
B2.grid(row=4, column=2)

# Keeps GUI running till closed
gui.after(1000, get_stock_price)
gui.mainloop()