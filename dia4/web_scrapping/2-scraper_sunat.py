import requests
from bs4 import BeautifulSoup

URL ='https://www.sunat.gob.pe/'

response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.content,'html.parser')
    #<strong id="sell-rate">3.39</strong>
    precio_venta = soup.find('strong',id='sell-rate').get_text()
    print(f' precio venta dolares : {precio_venta}')