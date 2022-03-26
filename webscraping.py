import requests
from bs4 import BeautifulSoup
# 1st Example

# url = 'https://quotes.toscrape.com/'    #сохраняется адрес страницы, с которой будет поступать информация
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')  #Получаем текстовый код страницы в формате lxml
# quotes = soup.find_all('span', class_='text') #Найдем все теги span с классом text на странице
# authors = soup.find_all('small', class_='author') #каждый автор заключен в тег <small> с классом author
# tags = soup.find_all('div', class_='tags')
#
# # Затем в цыкле перебираем все теги и классы
# for i in range(0, len(quotes)):
#     print(quotes[i].text)
#     print('--' + authors[i].text)
#     tagsforquote = tags[i].find_all('a', class_='tag')
#     for tagforquote in tagsforquote:
#         print(tagforquote.text)
#     print('\n')

# #2nd Example
# url = 'https://scrapingclub.com/exercise/list_basic/?page=4'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
#
#
# for n, i in enumerate(items, start=1):
#     itemName = i.find('h4', class_='card-title').text.strip()
#     itemPrice = i.find('h5').text
#     print(f'{n}:  {itemPrice} за {itemName}')

#3 Example
url = 'https://www.lamoda.kz/c/831/default-sports-women/?zbs_content=js_w_icons_869374_kz_2502_w_icons'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='x-product-card-description__brand-name')

for n, i in enumerate(items, start=1):
    itemName = i.find('div', class_='x-product-card-description__brand-name')
    print(f'{n}: {itemName}')
