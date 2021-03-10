import requests
import math
from bs4 import BeautifulSoup
import time
start = time.time()

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
# US STOCKS
def extract_data(r):
    price = r.find('span',{'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).get_text()
    company = r.find('h1', {'class': 'D(ib) Fz(18px)'}).get_text()
    price = float(price)
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
# KR STOCKS
def extract_data_kr(r):
    price = r.find('span',{'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).get_text()
    price = price.replace(',','')
    price = math.floor(float(price))
    price = (price/1104)
    price = round(price,2)
    company = r.find('h1', {'class': 'D(ib) Fz(18px)'}).get_text()
    return {'company' : company, 'price' : price}
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
    datas = datas + kr_datas
    percentage = 2.4;
    return datas, percentage
init()
print("time :", time.time() - start) 