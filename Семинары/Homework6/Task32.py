# Задача 32: Определить индексы элементов массива (списка), значения которых
#  принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import os
import random

os.system('cls')

max = int(input('Введите максимальное значение: '))
min = int(input('Введите минимальные значение: '))

list = [random.randint(-100, 100) for _ in range(15)]

print(list)

index_list = [i for i, v in enumerate(list) if min < v < max]
print(f'индексы чисел в промежутке больше {min} и меньше {max}:')
print(index_list)