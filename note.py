import requests
import math
from bs4 import BeautifulSoup

URL = 'https://finance.yahoo.com/'

CODES = {
    'apple': 'AAPL',
    'luminar': 'LAZR',
    'nvidia': 'NVDA',
    'velodyne': 'VLDR',
    'tesla': 'TSLA',
    'unity': 'U'
}
KR_CODES = {
    'hyundae_car': '005380.KS',
    'naver': '035420.KS',
    'hyundae_autoever': '307950.KS',
    'samsung_sdi': '006400.KS',
    'kakao': '035720.KS',
}

def extract_data(r):
    price = r.find('span',{'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).get_text()
    company = r.find('h1', {'class': 'D(ib) Fz(18px)'}).get_text()
    price = float(price)
    return {'company' : company, 'price' : price}

def extract_data_kr(r):
    price = r.find('span',{'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).get_text()
    price = price.replace(',','')
    price = math.floor(float(price))
    price = (price/1104)
    price = round(price,2)
    company = r.find('h1', {'class': 'D(ib) Fz(18px)'}).get_text()
    print(price)
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

def get_price_kr():
    kr_datas = []
    for company in KR_CODES:
        selected = KR_CODES[company]
        raw = requests.get(f'{URL}/quote/{selected}')
        soup = BeautifulSoup(raw.text, 'html.parser')
        results = soup.find_all('div',{'class':'quote-header-section'})
        for r in results:
            data = extract_data_kr(r)
            kr_datas.append(data)
    return kr_datas
            
def init():
    datas = get_price()
    kr_datas = get_price_kr()

    sum_up = [];
    kr_sum_up = [];

    for data in datas:
        prices = float(data['price'])
        sum_up.append(prices)
    
    for data in kr_datas:
        prices = int(data['price'])
        kr_sum_up.append(prices)
    
    # current price
    AAPL_price = sum_up[0]
    LAZR_price = sum_up[1]
    NVDA_price = sum_up[2]
    VLDR_price = sum_up[3]
    TSLA_price = sum_up[4]
    U_price = sum_up[5]
    # my invest
    my_invest = 1400
    
    # kr current price
    HYUNDAE_C_price = kr_sum_up[0]
    NAVER_price = kr_sum_up[1]
    HYUNDAE_A_price = kr_sum_up[2]
    SAMSUNG_price = kr_sum_up[3]
    KAKAO_price = kr_sum_up[4]
    # kr invest
    kr_invest = (2048500/1104);
    
    current_price = AAPL_price + LAZR_price + NVDA_price + VLDR_price + TSLA_price + U_price
    kr_current_price = HYUNDAE_C_price + NAVER_price + HYUNDAE_A_price + SAMSUNG_price + KAKAO_price

    current_price = current_price + kr_current_price
    my_invest = my_invest + kr_invest

    profit = (current_price - my_invest)/(my_invest*100)
    percentage = round(profit*10000,2)

    datas = datas + kr_datas
    
    return datas, percentage

init()