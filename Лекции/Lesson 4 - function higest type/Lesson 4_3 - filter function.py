# Функция filter
# Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для которых функция вернула True.

import os
import random   

os.system ('cls')

data = list (random.randint(1, 20) for _ in range (1,20))
print (data)

res = list(filter(lambda x: x % 10 ==5, data)) # при true записывает/пропускает через себя
print (res)