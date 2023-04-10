# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
#  почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как,
# например, у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) `
# **Вывод:**
# 1 2 3 4 5 6

# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

import os
os.system('cls')


def print_tabel(rows, colums, chose):
    for x in range(1, rows + 1):
        list = []
        for y in range(1, colums + 1):
            number = operation(x, y, chose)
            list.append(number)
        print(list)
        # print(''.join(list))


def operation(x1, y1, chose):
    if chose == '1':
        return x1*y1
    elif chose == '2':
        return round(x1/y1, 1)
    elif chose == '3':
        return round(y1/x1, 1)
    elif chose == '4':
        return x1+y1
    elif chose == '5':
        return x1-y1
    elif chose == '6':
        return y1-x1
    else:
        return ':('


num_rows = int(input('Введите количество строк: => '))
num_colums = int(input('Введите количество столбцов: => '))
global chose

print('Введите, какую функцию следует использовать:')
print('[1] - х*y')
print('[2] - х/y')
print('[3] - y/х')
print('[4] - х+y')
print('[5] - х-y')
print('[6] - y-x')
chose = input('=> ')

print_tabel(num_rows, num_colums, chose)
