documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def people(number):
    doc_number = 0  # Вывод имени
    for num in documents:
        spis = list(num.values())
        if spis[1] == number:
            doc_number = spis[2]
            print(doc_number)
            break
    if doc_number == 0:
        print('Данного документа не сущетсвует')


def shelf(number):  # Вывод номера полки
    num_shelf = 0
    for key in directories:
        for num_doc in directories.get(key):
            if num_doc == number:
                num_shelf = key
                break
        if num_shelf != 0:
            break
    if num_shelf != 0:
        print(f'Номер полки: {num_shelf}')
    else:
        print('Данного документа не существует')


def list_command():  # Вывод всех документов
    for num in documents:
        spis = list(num.values())
        print(f'{spis[0]} "{spis[1]}" "{spis[2]}"')


def add(number, type, name, num_shelf):  # Добавление документа
    if num_shelf in list(directories.keys()):
        documents.append([{"type": type, "number": number, "name": name}])
        directories.get(num_shelf).append(number)
        print('Документ добавлен')
    else:
        print('Полки с данным номером не существует')

def people_all():
    for document in documents:
        try:
            print(document['name'])
        except KeyError:
            print(f'У документа {document["number"]} нет поля name')

def func_input():
    command = input('Введите команду: p, s, i, a, d ')  # Обработка вводда комманды
    if command == 'p':
        people(input('Введите номер документа: '))
    elif command == 's':
        shelf(input('Введите номер документа: '))
    elif command == 'i':
        list_command()
    elif command == 'a':
        add(input('Введите номер документа: '), input('Введите тип документа: '), input('Введите имя: '),
            input('Введите номер полки: '))
    elif command == 'd':
        people_all()
    else:
        print('Данной команды не существует')


func_input()
