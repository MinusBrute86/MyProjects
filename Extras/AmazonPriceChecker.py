import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/PlayStation-4-Pro-1TB-Console/dp/B01LOP8EZC?pf_rd_r=AT680BFPS89CBANT6GZ4&pf_rd_p=c5b6893a-24f2-4a59-9d4b-aff5065c90ec&pd_rd_r=25679c36-ea45-4165-ac65-2723b773c908&pd_rd_w=BdZkx&pd_rd_wg=ydMfe&ref_=pd_gw_ci_mcx_mr_hp_d'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('user', 'pass')

    subject = 'Test'
    body = 'Testing Python file'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'email1',
        'email2',
        msg
    )
    print('email has been sent')

    server.quit()


def price_check():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = price[0:]
    if converted_price > 1:
        send_mail()
    print(converted_price)


price_check()
