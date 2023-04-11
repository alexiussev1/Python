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