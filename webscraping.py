import requests
import re
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
url = 'https://question-it.com/questions/1944385/kodirovka-pycharm-55-utf-8?'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# Метод title получает титул страницы <title>
# title = soup.title

# print(title)
# print(title.text)
# print(title.string)

# Методы .find() .find_all() поиска по тегу
# page_h1 = soup.find("a")
# print(page_h1)
# page_all_h1 = soup.find_all("a")
# #print(page_all_h1)
# for item in page_all_h1:
#     print(item.text)
# # Можно конкретизировать данный поиск указав кроме тега так же и класс
# autor = soup.find_all("span", class_ = "author")
#
# print(autor)
#
# for item in autor:
#     print(item.text)
# Передача словоря в атрибуты фильтрации поиска где с помощью пары ключь - значение указываем параметры отбора
# find_all_spans_in_misc = soup.find(class_="misc").find_all("span")
# print(find_all_spans_in_misc[1].text)
# for item in find_all_spans_in_misc:
#     print(item.text)

find_a_by_text = soup.find("div", text=re.compile("ответ"))
print(find_a_by_text)

find_by_text_all = soup.find_all("a", text=re.compile(("[Кк]одировку")))
for text in find_by_text_all:
    print(text.text)



