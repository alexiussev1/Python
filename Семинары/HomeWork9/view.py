import text_fields as txt


def main_menu() -> int:
    print('''Главное меню
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход''')

    # choise = ''

    while True:
        choise = input('Выберите пунтк меню: ')
        if choise.isdigit() and 0 < int(choise) < 9:
            return int(choise)
        else:
            print('Введите число от 1 до 8')

def change_menu() -> int:
    print('''Изменить контакт
    1. ФИО
    2. Телефон
    3. Заметки
    4. Все поля''')

    # choise = ''

    while True:
        choise = input('Выберите пунтк меню: ')
        if choise.isdigit() and 0 < int(choise) < 5:
            return int(choise)
        else:
            print('Введите число от 1 до 45')


def print_info(message: str):
    print('\n'+'-'*len(message))  # черточки над сообщением  длиной сообщения
    print(message)
    print('-'*len(message) + '\n')  # черточки под сообщением длиной сообщения


# внутри списка обозначаем словарики
def show_contacts(book: list[dict], message: str):
    if book:                                                    # правда -и список полный, ложь - список пустой
        print('\n' + '-' * 67)
        # сразу индекс элемента и его значение
        for n, contact in enumerate(book, 1):
            print(f'{n:>3}.{contact.get("name"):<30}'
                  f'{contact.get("phone"):<20}'
                  f'{contact.get("comment"):<20}')
        print('\n' + '-' * 67)
    else:
        print(message)


def new_contact() -> dict:
    print()
    name = input(txt.new_name)
    phone = input(txt.new_phone)
    comment = input(txt.new_comment)
    print()
    return {'name': name, 'phone': phone, 'comment': comment}


def find_contact() -> dict:
    print()
    name = input(txt.find_name)
    phone = input(txt.find_phone)
    print()
    return {'name': name, 'phone': phone}


def number_contact(book: list[dict],  message: str):
    print()
    number = -1
    while number > len(book) or number < 1:
        number=int(input(txt.del_position))
        if number > len(book) or number < 1: print(message)
    return(number)

def confir(massage: str) -> bool:
    print()
    answer = input(massage + ' y/n? -> ')
    if answer.lower() == 'y':
        return True
    else:
        return False
