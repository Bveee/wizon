import requests
from bs4 import BeautifulSoup
import re


class Content:
    def __init__(self, url, title, price, dict_phone):
        self.url = url
        self.title = title
        self.price = price
        self.dict_phone = dict(dict_phone)


# def get_page(url):     # если надо скачать с сайта
#     headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'\
#         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/'\
#         '537.36'}
#     req = requests.get(url, headers=headers)
#     return BeautifulSoup(req.text, 'html.parser')


def get_file(html):
    with open(html_path, 'r') as f:  # из файла
        html = f.read()
    return BeautifulSoup(html, 'html.parser')


def scrape_ozon(url):
    bs = get_file(url)
    dict_phone = dict()
    for index, item in enumerate(bs.findAll('div', {'class': 'bi3 bi5'})):
        title = item.find('span', {'class': 'a7y a8a2 a8a6 a8b2 f-tsBodyL bj5'}).text
        price = int(item.find('span', {'class': re.compile('ui-p5 ui-p8.*')}).text[:-2].replace(u'\u2009', ''))
        dict_phone.update({index: {'title': title, 'price': price}})
    return Content(url, title, price, dict_phone)


def scrape_wildberries(url):
    bs = get_file(url)
    dict_phone = dict()
    for index, item in enumerate(bs.findAll('div', {'class': 'product-card__brand'})):
        title = item.find('span', {'class': 'goods-name'}).text
        price = int(item.find('span', {'class': re.compile('.*-price')}).text.strip()[:-2].replace(u'\xa0', ''))
        dict_phone.update({index: {'title': title, 'price': price}})
    return Content(url, title, price, dict_phone)


# search = input('Напишите модель телефона: ').replace(' ', '+') # какой телефон искать

# url = 'https://www.ozon.ru/category/smartfony-15502/'\    # запрос поиска для OZON
#     '?from_global=true&sorting=rating&text='+search
# print(url)

html_path = 'OZON.html'
content = scrape_ozon(html_path)
print(content.dict_phone)

# url = 'https://www.wildberries.ru/catalog/0/'\    # запрос поиска для wildberries
#     'search.aspx?search='+search+'&xsubject=515&sort=rate'
# print(url)
print()

html_path = 'Wildberries.html'
content = scrape_wildberries(html_path)
print(content.dict_phone)
