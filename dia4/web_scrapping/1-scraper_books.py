import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

URL = 'http://books.toscrape.com'

response = requests.get(URL)

if response.status_code == 200:
    data = response.content
    #print(data)
    soup = BeautifulSoup(response.content,'html.parser')
    books = soup.find_all('article',class_='product_pod')
    #print(books[0])
    rows = []
    for book in books:
        titulo = book.find('h3').find('a')['title']
        precio = book.find('p',class_='price_color').get_text().strip()
        disponibilidad = book.find(
            "p", class_="instock availability"
        ).text.strip()
        imagen = book.find("img")["src"]
        rows.append([titulo,precio,disponibilidad,imagen])
        
    headers = ['Titulo','Precio','Disponibilidad','Link','Imagen']
    print(tabulate(rows,headers,tablefmt='grid'))