import re
import requests as req
from bs4 import BeautifulSoup as bs

webpage = req.get('https://finance.yahoo.com/quote/AAPL/history?p=AAPL&guccounter=1')
content = webpage.content
soup = bs(content,'html.parser')

row_data = soup.find_all('tr', class_='BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)')

for i in range(len(row_data)):
    parse_data = row_data[i].find_all('td')
    stock_date = parse_data[0].text
    try:
        stock_price_closing = 'closing price: ' + parse_data[4].text
    except IndexError:
        stock_price_closing = parse_data[1].text
    print('%s, %s' % (stock_date, stock_price_closing))
