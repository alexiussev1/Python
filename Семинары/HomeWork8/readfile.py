def open_file():
    file_name = input('<введите любое значение>')
    file_name = 'Семинары\HomeWork8\phone book.txt'
    file = open(file_name, 'r', encoding='UTF-8')
    data = file.readlines()
    file.close

    for i in range(0, len(data)):
        temp = data[i].split(';')  # .remove('\n','')
        temp[2] = temp[2].removesuffix('\n')
        data[i] = temp
    return data


def save_file(data):
    data_str = ''

    for i in range(0, len(data)):
        if data[i][0] != '':
            temp = data[i]
            data_str = data_str+temp[0]+';' + temp[1]+';' + temp[2]+'\n'

    with open('Семинары\HomeWork8\phone book.txt', 'r+', encoding='UTF-8') as data1:
        data1.write(data_str)
