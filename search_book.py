# Импорт библиотек
from bs4 import BeautifulSoup #Библиотека для парсинга страниц
import requests #Библиотека для отправки запросов

url = 'http://books.toscrape.com/catalogue/category/books/classics_6/index.html'

page = requests.get(url)

allBooks = [] #Массив, где будем хранить нужную часть html страницы

book = BeautifulSoup(page.text, "html.parser") #Записываем в переменную book нашу страницу
allBooks = book.find_all('article', class_='product_pod') #Ищем на странице тег article с классом product_pod

found_books = {} #Словарь, где будут хранится найденные книги

def search_books():
    for data in allBooks:
        title = data.find('h3').find('a')['title'] #Находим тег h3 и название берем название из атрибута title тега a, тк там хранится полное название книги
        price = float(data.find('p', class_='price_color').get_text().replace('Â£', '')) #Находим тег p с классом price_color и записываем стоимость книги
        found_books[title] = price #Записываем полученные данные в словарь, для дальнейшего использования

#Вывод полученного результат
def output_books():
    print('Полученный список книг:')
    for key, value in found_books.items():
        print(f'Название: {key}, Цена: £{value}')
    print('')

#Вывод книг, где стоимость будет меньше заданной цены
def max_price():
    search_books() #Вызываем функцию поиска книг, для записи данных
    max = float(input('Введите максимальную стоимость книги: '))
    print(f'Cписок книг стоимостью меньше £{max}:')
    #Цикл для поиска книг по условию
    for key, value in found_books.items(): 
        if (value <= max):
            print(f'Название: {key}, Цена: £{value}')
    print('')

#Меню программы
def start():
    while True:
        key = int(input(f'[1] Поиск книг на странице\n[2] Поиск книг по стоимости\n[3] Выход\nВвод: '))

        match key:
            case 1: search_books(), output_books() #При выборе 1 - запускаем поиск книг, ожидаем действия от польз. 
            case 2: max_price() #При выборе 2 - запрашиваем макс стоимость, запускаем поиск книг, ожидаем действия от польз. 
            case 3: return  #Выходим из цикла
            case _: print('Такого варианта нет :(\n') #При вводе других вариантов, выводи предупреждение и ожидаем действия от польз.
