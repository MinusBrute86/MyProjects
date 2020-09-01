from yahoo_fin.stock_info import get_live_price
import time

while True:
    tesla_price = get_live_price("tsla")
    print("\nTSLA\t" + str(tesla_price))
    time.sleep(1)
print("error")