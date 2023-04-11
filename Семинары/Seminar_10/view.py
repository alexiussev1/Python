import text_fields as txt

def main_menu() -> int:
    print('''Главное меню
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Созлать контак
    5. Нати контакт
    6. Изсенить контакт
    7. Удалить контакт
    8. Выход''')

    choise = ''

    while True:
        choise = input('Выберите пунтк меню: ')
        if choise.isdigit() and 0 < int(choise) < 9:
            return int(choise)
        else:
            print('Введите число от 1 до 8')


def print_info(massege: str):
    print('\n'+'-'*len(massege))
    print(massege)
    print('-'*len(massege) + '\n')


# внутри списка обозначаем словарики
def show_contacts(book: list[dict], message: str):
    if book:                                                    # правда -и список полный, ложь - список пустой
        print('\n' + '-' * 63)
        # сразу индекс элемента и его значение
        for n, contact in enumerate(book, 1):
            print(f'{n:>3}. {contact.get("name"): < 20}'
                  f'{contact.get("phone"): < 20}'
                  f'{contact.get("comment"): < 20}')
        print('\n' + '-' * 63)
    else:
        print(message)


def new_contact() -> dict:
    print()
    name = input(txt.new_name)
    phone = input(txt.new_phone)
    comment = input(txt.new_comment)
    print()
    return {'name': name, 'phone': phone, 'comment': comment}

def confir(massage: str) -> bool:
        print()
        answer = input(massage + ' y/n? -> ')
        if answer.lower() =='y':
            return True
        else:
            return False