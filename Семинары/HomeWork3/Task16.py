# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

import os
import random

os.system ("cls")

Lenght_for_Array = int(input ("Введите длину массива:"))
list_1 = [random.randint(1, 5) for i in range(0, Lenght_for_Array)]
print (list_1)
Find_Number = int(input ("Введите искомое число из списка выше: "))
print ("Цифра встречается в списке: ", list_1.count(Find_Number), "раз(а) ")