# Функция — это фрагмент программы, используемый многократно

# Задание: Необходимо создать функцию sumNumbers(n), которая будет считать
# сумму всех элементов от 1 до n.

import os
os.system("cls")


def sum_numbers(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    print(summa)


sum_numbers(5)


def sum_numbers(n):
    summa = 0
    for i in range(1, n+1):
        summa *= i
    return summa


print(sum_numbers(10))


def sum_numbers(n):
    summa = 0
    for i in range(1, n+1):
        summa -= i
    return summa


a = sum_numbers(6)
print(a)


def sum_numbers(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa
    print("STOP")  # не выводится так как после return и VS коде тоэе не посвечивает


a = sum_numbers(9)
print(a)


def sum_numbers(n, y="Hello"):
    print(y)
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa


a = sum_numbers(3)
print(a)


def sum_numbers(n, y="Hello"):
    print(y)
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa


a = sum_numbers(7, "qwerty")
print(a)


def sum_str(*args):  # * - передача неограниченного кол-ва аргментов
    res = ''
    for i in args:
        res += i
    return res


print(sum_str("q", "e", "l"))
print(sum_str("q", "e", "l", "r", "t"))
print(sum_str("1", "8", "9"))
