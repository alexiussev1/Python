phone_book = []
start_phone_book = []
# 'Семинары\Seminar_10\phone_book.txt'
PATH = 'Семинары\Seminar_9\phone_book.txt'


def get_pb():
    global phone_book
    return phone_book


def load_file():
    global phone_book, start_phone_book
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(';')
        phone_book.append({'name': contact[0],
                           'phone': contact[1],
                           'comment': contact[2]})
    start_phone_book = phone_book.copy


def save_file():
    global phone_book
    data = []
    for contact in phone_book:
        data.append(';'.join([value for value in contact.values()]))
    data = '\n'.join(data)
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write(data)


def add_contact(contact: dict):
    global phone_book
    phone_book.append(contact)


def exit_pb():
    global phone_book, start_phone_book
    if phone_book == start_phone_book:
        return False
    else:
        return True


def find(find_info: dict):
    global phone_book
    temp_dict = []

    if find_info['name'] != "" and find_info['phone'] != "":
        for item in phone_book:
            if find_info['name'] in item.values() and find_info['phone'] == item.values():
                temp_dict.append(item)

    elif find_info['name'] != "" and find_info['phone'] == "":
        for item in phone_book:
            if find_info['name'] in item.values():
                temp_dict.append(item)

    elif find_info['name'] == "" and find_info['phone'] != "":
        for item in phone_book:
            if find_info['phone'] in item.values():
                temp_dict.append(item)

    return temp_dict


def delete(number_contact: int):
    global phone_book
    phone_book.pop(number_contact-1)


def change(number_contact: int, position_change: int):
    global phone_book
    index = number_contact - 1
    temp_dict = phone_book[index]

    choise = position_change

    match choise:
        case 1:
            temp_dict['name'] =input('Введите ФИО: ')
        case 2:
            temp_dict['phone'] =input('Введите телефон: ')
        case 3:
            temp_dict['comment'] =input('Введите заметку: ')
        case 4:
            temp_dict['name'] =input('Введите ФИО: ')
            temp_dict['phone'] =input('Введите телефон: ')
            temp_dict['comment'] =input('Введите заметку: ')

    phone_book[index] = temp_dict