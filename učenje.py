import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "http://www.bolha.com/racunalnistvo/igricarstvo-gaming/?page=" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('a', title = True):
            href = link.get('href')
            title = link.string
            link = 'http://www.bolha.com' + href
            #print(title)
            print(link)
            #get_single_item_data(href)
        page += 1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for item_name in soup.findAll('div'):
        print(item_name.string)

trade_spider(1)
