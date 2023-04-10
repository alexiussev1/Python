# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных

import os, viwe, readfile, contakts

os.system('cls')

while True:
    choise = viwe.main_menu()

    if choise == 1:  # Открыть файл
        os.system('cls')
        print('Открыть файл')
        data = readfile.open_file()

    elif choise == 2:  # Сохранить файл
        os.system('cls')
        print('Сохранить файл')
        readfile.save_file(data)

    elif choise == 3:  # Показать все контакты
        os.system('cls')
        print('Показать все контакты:')
        contakts.show_contacts(data)
        print(type(data))

    elif choise == 4:  # Создать контакт
        os.system('cls')
        print('Создать контакт')
        contakts.new_contact(data)

    elif choise == 5:  # Найти контакт
        os.system('cls')
        print('Найти контакт')
        contakts.find_contact(data)

    elif choise == 6:  # Изменить контакт
        os.system('cls')
        print('Изменить контакт')
        contakts.chainge_contact(data)

    elif choise == 7:  # Удалить контакт
        os.system('cls')
        print('Удалить контакт')
        contakts.del_contact(data)

    elif choise == 8:  # Выйти
        os.system('cls')
        print('Выйти')
        break
