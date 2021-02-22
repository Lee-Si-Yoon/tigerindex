# tigerindex

### 데이터 변경
수기입력 할 수 있는 데이터는 두가지입니다

(지금 접속불가에 매우 가까운 로딩속도를 보이기에... 종목 추가는 권하지 않습니다. 되려 한두개 제외시키신다면 속도 빨라집니다)

1. 환율
```
# note.py
def extract_data_kr(r):
    price = r.find('span',{'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).get_text()
    price = price.replace(',','')
    price = math.floor(float(price))
    price = (price/1104)
= 여기서 price/1104 에 환율에 맞는 숫자를 넣어주시면 됩니다
``` 
2. 수익률
```
# note.py
def init():
    datas = get_price()
    kr_datas = get_price_kr()
    datas = datas + kr_datas
    percentage = 3.4;
    return datas, percentage
= 여기서 percentage 에서 수익률 수기로 입력해주시면 됩니다
```

### 내용 추가 및 css 수정

1. 내용추가
```
# static/templates/index.html
<div class="news">
  <div class="news__container">
     <h3>Tiger Index, 호랑이 지수는 모빌리티 세계를 연결합니다.</h3>
      .......(중략) <= 여기에 p태그로 내용 입력해주시면 됩니다
   </div>
</div>
```
```
유의점 
1. p 및 h3 태그만 css 적용되어있습니다
2. 다른 태그 사용시 css 직벚 추가하시거나 저한테 연락바랍니다
```
2. 사진추가
```
# static/templates/index.html
<img src="{{url_for('static', filename='icons/imgs/news3.jpg')}}" alt="news" class="news3"/>
= 보시면 아시겠지만 복사 붙여넣기로 추가하실 수 있고 img의 src와 class만 숫자 바꿔주시면 됩니다
```
