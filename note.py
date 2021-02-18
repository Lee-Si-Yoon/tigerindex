import requests
import math
from bs4 import BeautifulSoup

URL = 'https://finance.yahoo.com/'

CODES = {
    #'hyundae_car': '005380.KS',
    #'naver': '035420.KS',
    #'hyundae_autoever': '307950.KS',
    #'samsung_sdi': '006400.KS',
    #'kakao': '035720.KS',
    'apple': 'AAPL',
    'luminar': 'LAZR',
    'nvidia': 'NVDA',
    'velodyne': 'VLDR',
    'tesla': 'TSLA',
    'unity': 'U'
}
def extract_data(r):
    price = r.find('span',{'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).get_text()
    company = r.find('h1', {'class': 'D(ib) Fz(18px)'}).get_text()
    return {'company' : company, 'price' : price}

def get_price():
    datas = []
    for company in CODES:
        selected = CODES[company]
        raw = requests.get(f'{URL}/quote/{selected}')
        soup = BeautifulSoup(raw.text, 'html.parser')
        results = soup.find_all('div',{'class':'quote-header-section'})
        for r in results:
            data = extract_data(r)
            datas.append(data)
    return datas
            
def init():
    datas = get_price()
    sum_up = [];

    for data in datas:
        prices = float(data['price'])
        sum_up.append(prices)
    
    # current price
    AAPL_price = sum_up[0]
    LAZR_price = sum_up[1]
    NVDA_price = sum_up[2]
    VLDR_price = sum_up[3]
    TSLA_price = sum_up[4]
    U_price = sum_up[5]
    # my invest
    my_invest = 1700;

    current_price = AAPL_price + LAZR_price + NVDA_price + VLDR_price + TSLA_price + U_price;

    profit = (current_price - my_invest)/(my_invest*100)
    percentage = round(profit*10000,2)
    
    return datas, percentage

init()



"""
import requests
import json
import math
import time
from bs4 import BeautifulSoup

# authentic
API_KEY = '28d8e6e184a9c2e328bce1d0c20fbeff'
STOCK_CODE = ['AAPL','LAZR','NVDA','VLDR','TSLA','U']
# demo
#API_KEY = 'demo'
#STOCK_CODE = ['AAPL','AAPL','AAPL','AAPL','AAPL','AAPL']

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
"""