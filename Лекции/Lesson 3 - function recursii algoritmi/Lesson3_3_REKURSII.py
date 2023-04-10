# Рекурсия

# С рекурсией Вы знакомы с C#, в Python она ничем не отличается, давай рассмотрим
# следующую задачу: Пользователь вводит число n. Необходимо вывести n - первых
# членов последовательности Фибоначчи.
# Напоминание: Последовательно Фибоначчи, это такая последовательность, в
# # которой каждое последующее число равно сумму 2-ух предыдущих

# 💡 При описании рекурсии важно указать, когда функции надо
# остановиться и перестать вызывать саму себя. По-другому говоря, необходимо
# указать базис рекурсии

import os
os.system("cls")


def fibanachi(n):
    if n in [1,2]:  #помните, обяхательное уставьте условие по выходу из рекрсии в начале
        return 1
    return fibanachi(n-1) + fibanachi(n-2)

list_1=[]
for i in range(1,10):
    list_1.append(fibanachi(i))
print(list_1)