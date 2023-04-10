# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических
# операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4

import os
os.system("cls")

def sum_one_plus(n1, n2):
    global i
    if n1 > 0:
        i+=1
        sum_one_plus(n1-1, n2)
    elif n2 > 0:
        i+=1
        sum_one_plus(n1, n2-1)
    return i

number_a = int(input("Введите число А: "))
number_b = int(input("Введите число B: "))

i=0
print(f"{number_a} + {number_b} = {sum_one_plus(number_a, number_b)}")
