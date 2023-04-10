# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод: Вывод:
# 0 2

import random
import os

os.system("cls")

n_list1 = int(input("Введите размер списка: "))
list_1 = [random.randint(1, 10) for _ in range(0, n_list1)]
count = 0
for i in range(2, len(list_1)-1):
    if list[i] < list_1[i+1] + list_1[i-1]:
        count += 1

print(count)
