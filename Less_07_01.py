def read_csv(filename: str):
    data = []
    fields = ["ИД", "Фамилия", "Имя/Отчество", "Должность", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
    "1. Отобразить весь справочник\n"
    "2. Найти абонента по фамилии\n"
    "3. Найти абонента по номеру телефона\n"
    "4. Добавить абонента в справочник\n"
    "5. Сохранить справочник в текстовом формате\n"
    "6. Закончить работу")
    choice = int(input())
    return choice

def result(abonent):
    print(f'{abonent["ИД"]},{abonent["Фамилия"]},{abonent["Имя/Отчество"]},{abonent["Должность"]},{abonent["Телефон"]},{abonent["Описание"]}')

def all_directory(phone_book):
    for i in phone_book:
        result(i) 
    menu(phone_book)     

def search_family(phone_book):
    family = input('Введите фамилию для поиска абонента: ')
    for i in phone_book:
        if i['Фамилия'] == family:
            result(i)
    menu(phone_book)

def search_num(phone_book):
    num = input('Введите телефон для поиска абонента: ')
    for i in phone_book:
        if i['Телефон'] == num:
            result(i)
            menu(phone_book)

def add_abonent(phone_book):
    fam = input('Фамилия: ')
    name = input('Имя/Отчество: ')
    job_title = input('должность: ')
    num = input('Телефон: ')
    other = input('Описание: ')

    with open('less_07_01_01.csv', 'a', encoding='utf-8') as data:
	    data.write(f'{len(phone_book) + 1 },{fam},{name},{job_title},{num},{other}\n')

def doc_txt(phone_book):
    for i in phone_book:
        with open('less_07_01_02.txt','a', encoding='utf-8') as data:
	        data.write(f'{i["ИД"]}. {i["Фамилия"]} {i["Имя/Отчество"]}, {i["Должность"]}, т.{i["Телефон"]}, {i["Описание"]}\n')

def menu(phone_book):
    num_menu = show_menu()
    if num_menu == 1: 
        phone_book = read_csv('less_07_01_01.csv')
        all_directory(phone_book)
    if num_menu == 2: 
        phone_book = read_csv('less_07_01_01.csv')
        search_family(phone_book)
    if num_menu == 3:
        phone_book = read_csv('less_07_01_01.csv')
        search_num(phone_book)
    if num_menu == 4:
        phone_book = read_csv('less_07_01_01.csv')
        add_abonent(phone_book)
        menu(phone_book)
    if num_menu == 5:
        phone_book = read_csv('less_07_01_01.csv')
        doc_txt(phone_book)
        menu(phone_book)
    if num_menu == 6:
        print('работа со справочником завершена')

phone_book = read_csv('less_07_01_01.csv')
menu(phone_book)