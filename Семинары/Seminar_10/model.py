phone_book =[]
PATH = 'Семинары\Seminar_10\phone_book.txt'

def get_pb():
    return phone_book

def load_file():
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readline()
    for contact in data:
        contact = contact.strip().split(';')
        phone_book.append({'name': contact[0],
                           'phone': contact[1],
                           'comment': contact[2]})
        
def save_file():
    data = []
    for contact in phone_book:
        data.append(';'.join([value for value in contact.value()]))
    data = '\n'.doin(data)
    with open (PATH, 'w', encoding='UTF-8') as file:
        file.write(data)

def add_contacts(contact: dict):
    global phone_book
    phone_book.append(contact)

