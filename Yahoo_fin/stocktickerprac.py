from yahoo_fin.stock_info import get_live_price
import time

tick_sym = input("Enter stock ticker: ")

while True:
    price = get_live_price(tick_sym)
    print(str(tick_sym) + " " + str(price))
    time.sleep(1)
