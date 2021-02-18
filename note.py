import requests
import json
import math
import time
from bs4 import BeautifulSoup

# authentic
API_KEY = '28d8e6e184a9c2e328bce1d0c20fbeff'
#STOCK_CODE = ['AAPL','LAZR','NVDA','VLDR','TSLA','U']
# demo
#API_KEY = 'demo'
STOCK_CODE = ['AAPL','AAPL','AAPL','AAPL','AAPL','AAPL']

API_URL = 'https://financialmodelingprep.com/api/v3/profile'

def get_price():
    datas = []
    for companys in STOCK_CODE:
        response = requests.get(f'{API_URL}/{companys}?apikey={API_KEY}')
        raw_json = json.loads(response.text)
        raw = raw_json[0]
        price = raw['price']
        name = raw['companyName']
        data = {'company':name,'price':price}
        datas.append(data)
    return datas


def init():
    datas = get_price()
    sum_up = []

    for data in datas:
        prices = data['price']
        sum_up.append(prices)
    
    #current
    AAPL_price = sum_up[0]
    LAZR_price = sum_up[1]
    NVDA_price = sum_up[2]
    VLDR_price = sum_up[3]
    TSLA_price = sum_up[4]
    U_price = sum_up[5]

    #my invest : enter your total price in $
    my_invest = 1700;
    current_price = AAPL_price + LAZR_price + NVDA_price + VLDR_price + TSLA_price + U_price;

    profit = (current_price - my_invest)/(my_invest*100)
    percentage = round(profit*10000,2)
    return datas, percentage

init()