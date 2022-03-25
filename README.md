# WebScraping

## Установка библиотек для парсинга
### Если в проекте еще не установленны библиотеки то в терминале Pycharm вводим
- pip install lxml
- pip install requests
- pip install beautifulsoup4

## Создание скрипта скрапинга
##### url = 'https://quotes.toscrape.com/'    #сохраняется адрес страницы, с которой будет поступать информация
##### response = requests.get(url)
##### soup = BeautifulSoup(response.text, 'lxml')  #Получаем текстовый код страницы в формате lxml
##### quotes = soup.find_all('span', class_='text') #Найдем все теги span с классом text на странице
##### authors = soup.find_all('small', class_='author') #каждый автор заключен в тег <small> с классом author
##### tags = soup.find_all('div', class_='tags')

# Затем в цыкле перебираем все теги и классы
##### for i in range(0, len(quotes)):
    ##### print(quotes[i].text)
    ##### print('--' + authors[i].text)
    ##### tagsforquote = tags[i].find_all('a', class_='tag')
    ##### for tagforquote in tagsforquote:
        ##### print(tagforquote.text)
    ##### print('\n')


