# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко
# он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются
# дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в
# программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке
# и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам

import os
os.system('cls')

string_with_vowels = 'аеёиоуэюиыя'

list_inside = list(input(
    'Введите стихотворение Вини-Пуха, слова отделяются деффисами, а строки пробелами:').lower().split())

for i in range(len(list_inside)):
    list_inside[i] = ''.join([char for char in list_inside[i] if char in string_with_vowels])

answeer = True

for i in range(1, len(list_inside)):
    if len(list_inside[i]) != len(list_inside[i-1]):
        answeer = False
        break

if answeer:
    print ('Парам пам-пам') # есть рифма
else:
    print ('Пам парам') # нет рифмы