import text_fields as txt # импортиреует весь файл text_fields  и называем его как txt

def main_menu() -> int:
    print(txt.main_menu)
    choise = '1'
    while True:
        if choise.isdigit() and 0 < int (choise)<9: # choise.isdigit() - True  если все значения цыфры (это цифра?)
            choise = int (input(txt.choise_menu))
            break
    return int(choise)