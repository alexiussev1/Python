# Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя
# используется пробел. Этот набор чисел будет считан в качестве строки. Как
# превратить list строк в list чисел?

import os
os.system ('cls')

# list_1 = input().split()                    #мое решение
# list_1=list(map(lambda x:int(x), list_1))   #мое решение


list_1 = '15 156 98 3 5 8 12 45'
print(list_1)

list_1=list(map(int, list_1.split()))
print(list_1)
