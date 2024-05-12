# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилиючеловека)
# 4. Использование функций. Ваша программане должна быть линейной
import os

filename = 'tel.txt'

def load_data():
    if os.path.isfile(filename): #проверяем есть ли такой файл,если есть, то открываем его или создаем новый
        with open(filename, encoding='utf-8') as f1:
            r = f1.readlines()   #загружаем все данные с файла построчно после их нужно перевести в нужный для обработки формат
            book = []
            for line in r:
                book.append(line.split())
        return book
    book = []
    return book

def add_tel(book):
    last_name = input('введите фамилию: ') 
    first_name = input('введите имя: ') 
    second_name = input('введите отчество: ') 
    tel = input('введите телефон: ') #добавляем новую запись
    with open(filename, 'a', encoding='utf-8') as f1:                          #открываем файл в форамте редактирования
        f1.write(f'{last_name} {first_name} {second_name} {tel} \n')           #загружаем запись в файл в формате строки
    book.append([last_name, first_name, second_name, tel])                 #добавляем в список новые данные, для дальнейшей обработки
    return book                                                            #обновляем список новыми данными


def show_book(book):
    for line in book:
        print((' ').join(line))


def search_phone(book, object):
    for line in book:
        if object in line:
            return (' ').join(line)
    return 'такой записи нет'


if __name__ == '__main__':   #сразу открывает программу
    book = load_data()
    while True:
        act = input('Меню:\n1 -добавить данные \n2 - искать данные \n3 - показать всю книгу\n4 - выход\nвыберите пукт меню: ')
        if act == '1':
            book = add_tel(book)  
        elif act == '2':
            object = input('Введите что выхотите найти: ')  
            print(search_phone(book,object))   
        elif act == '3':
            book = show_book(book)
        elif act == '4':
            break
        else:
            print('выберите пункт меню от 1 до 3')