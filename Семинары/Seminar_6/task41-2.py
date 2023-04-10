# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: Вывод:
# 1 2 3 2 3 2

import random
import os

os.system("cls")

n_size = int(input("Введите размер списка: "))
list_1 = [random.randint(1, 10) for _ in range(0, n_size)]
print(list_1)

count = 0
for i in list_1:
    for j in list_1:
        if i==j and list_1[i]==list[j]:
            list_1 = list_1.pop(i,j)
            count +=1
            i=0
            j=0

print (count)
    
