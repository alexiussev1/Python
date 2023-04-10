# Задача для самостоятельного решения
# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

import os
os.system('cls')

# list = [1, 2, 3, 5, 8, 15, 23, 38]    -  начал сам решать
# list_out=[[]]

# for i in list:
#     if list[i]%2==0:
#         list_out.append(list[i])
#         a=list[i]*list[i]
#         list_out.append(a)

# print (list_out)

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
# for i in data:  # перебирает значения элементов а не индексы!!!
#     if i % 2 == 0:
#         res.append((i, i**2)) # двойные скобки!!! так как в задаче в ответе фигурные скобки, надо применить кортеж
# print(res)


# ТЕПЕРЬ КОД ВЫШЕ ДЕЛАЕМ ЧЕРЕЗ lamba

def select(f, col):
    return [f(x) for x in col]

def where (f, col):
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where (lambda x: x%2==0, res)
print(res)
res = select(lambda x: (x, x**2),res)
print(res)