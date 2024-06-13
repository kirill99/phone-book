import re
from file import get_data_from_file, set_data_to_file

data = []


def get_commands():
    commands = {
        '/exit': ('Команда выхода из программы', stop),
        '/len': ('Команда выдаст кол-во данных в справочнике', command_len),
        '/add': ('Команда добавления данных', command_add),
    }

    return commands


def item_find(text: str):
    success_search_list = []

    for i in data:
        for item in i.items():
            sub = str(item[1])
            if sub.find(text.lower().strip()) != -1:
                success_search_list.append(' \n'.join(
                    [f'{j[0]} - {j[1]}' for j in i.items()]))
                break

    if not len(success_search_list):
        print('Поиск не дал результатов -_- ')
    else:
        print(f'Поиск удался, ^_^ Всего нашли {len(success_search_list)} совпадений')

        for k, v in enumerate(success_search_list):
            print(f'Совпадение №{k+1}\n')
            print(v)
            print('\n#################\n')


def command_add():
    dict_data = {}
    dict_data['full_name'] = input('Введите имя: ').lstrip().rstrip()
    check_phone = True
    while check_phone:
        phone = input('Введите телефон: ').strip().replace(
            '(', '').replace(')', '').replace('-', '')
        if len(phone) == 12:
            check_phone = False
            dict_data['phone'] = phone
        else:
            print('Вы ввели не верный номер телефона')
    check_email = True
    while check_email:
        email = input('Введите email: ')
        if re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email):
            check_email = False
            dict_data['email'] = email
        else:
            print('Вы ввели не верный email-адрес')
    dict_data['address'] = input('Введите адрес: ')

    set_data_to_file([str(i[1]) for i in dict_data.items()])

    print('Запись успешно добавлена')

    global data

    data = get_data_from_file()


def command_len():
    print(len(data))


def hello():
    """
    The `hello` function in Python prints a message explaining the functionality of a program for
    searching and managing contacts.
    """
    print(
        '''Данная программа может искать людей по своему справочнику\nТак же вы можете развивать базу номеров, телефонов, email и адресов\n'''
    )

    print('Вы можете попытаться осуществить поиск или ввести команду')
    print('\n')
    print('Искать людей вы можете')
    print('-> По ФИО')
    print('-> По адресу')
    print('-> По сотовому')
    print('-> По email-адресу')
    print('\n')
    print('--------------------')
    print('####################')
    print('--------------------')
    print('\n')
    print('Список команд доступен по команде /help')
    print('\n')
    print('Удачи!')


def good_bye():
    """
    The function `good_bye()` prints "До свидания!" to the console.
    """
    print("До свидания!")


def stop():
    """
    The function `stop` calls the `good_bye` function and then exits the program.
    """
    good_bye()
    exit()


def start():
    global data
    data = get_data_from_file()
    commands = get_commands()
    while True:
        input_text = input('-> ')

        if input_text in commands:
            commands[input_text][1]()

        elif input_text == '/help':
            for i in commands.keys():
                print(f'{i} - {commands[i][0]}')
        else:
            item_find(input_text)
