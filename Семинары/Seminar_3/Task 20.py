# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает
# количество элементов массива, больших предыдущего (элемента с предыдущим номером)
import random
numb_list = [random.randint(0, 20) for _ in range(20)]
print(numb_list)
count = 0
i=1
while i<=range(numb_list):
    if numb_list[i]>numb_list[i-1]:
        count=count+1
    i=i+1
print (count)

