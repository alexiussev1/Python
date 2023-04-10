def find_contact(data):
    find_word = input('Введите слово для поиска: ')
    temp = ['', '', '']

    for i in range(0, len(data)):
        temp = data[i]
        temp_str = temp[0]+temp[1]+temp[2]
        if find_word.upper() in temp_str.upper():
            print(data[i])
        else:
            print('Контакт не найден')


def new_contact(data):
    temp1 = ['', '', '']
    print('Ввелите данные контака: ')
    temp1[0] = input('ФИО: ')
    temp1[1] = input('номер телефона: ')
    temp1[2] = input('заметка: ')
    print(temp1)
    data.append(temp1)
    return data


def chainge_contact(data):
    temp1 = ['', '', '']
    find_word = input('Ввелите ФИО контака для изменения: ')
    for i in range(0, len(data)):
        temp1 = data[i]
        if find_word.upper() == temp1[0].upper():
            print('Ввелите заново данные контака: ')
            temp1[0] = input('ФИО: ')
            temp1[1] = input('номер телефона: ')
            temp1[2] = input('заметка: ')
            data[i] = temp1
            break
    print('Контакт не найден')


def del_contact(data):
    temp1 = ['', '', '']
    find_word = input('Ввелите ФИО контака для удления: ')
    for i in range(0, len(data)):
        temp1 = data[i]
        if find_word.upper() == temp1[0].upper():
            temp1[0] = ''
            temp1[1] = ''
            temp1[2] = ''
            data[i] = temp1
            print('Контакт удален')



def show_contacts(data):
    # print(data)
    print(*('{} {} {}'.format(*r) for r in data), sep='\n')
