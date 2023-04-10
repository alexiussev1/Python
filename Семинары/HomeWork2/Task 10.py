# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import os
import random
os.system("cls")

coins = int(input("Введите количество монет на столе: "))
coins_reshka = int(0)
coins_list = [random.randint(0, 1) for i in range(0, coins)]

#print(coins_list)
sum_reshka = int(0)

for i in range(len(coins_list)):
    if coins_list[i] == 1:
        sum_reshka += 1

sum_orel = coins-sum_reshka
print (" Монеты решкой - ", sum_reshka,"\n" ,"Монеты орлом - ", sum_orel)

if (sum_reshka<sum_orel):
    print ("Минимальное количесво монет, которые надо перевернуть: ", sum_reshka)
else:
    print ("Минимальное количесво монет, которые надо перевернуть: ", sum_orel)