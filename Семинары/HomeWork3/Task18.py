# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import os
import random
os.system("cls")

Lenght_for_Array = int(input("Введите длину массива:"))
list_1 = [random.randint(1, 10) for i in range(0, Lenght_for_Array)]
print(list_1)

Find_Number = int(input("Введите число: "))

list_dif = list_1.copy()

for i in range(len(list_1)):
    list_dif[i] = abs(list_1[i]-Find_Number)

min_index = list_dif.index(min(list_dif))
print ("Ближайшее число:", list_1[min_index])