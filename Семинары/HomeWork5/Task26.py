# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

import os
os.system("cls")


def step_in(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return step_in(x, n//2)*step_in(x, n//2)
    else:
        return step_in(x, n-1)*x

# def step_in(x, n):        # НЕ МОГУ ПОНЯТЬ ПОЧЕМУ НЕ РАБОТАЕТ ДАННОЕ ЛОГИЧЕСКИ ИНТУИТИВНОЕ ПОНИМАНИЕ))))
#     if n == 0:
#         return total
#     elif n > 0:
#         total = step_in(x, n-1)*x


number_a = float(input("Введите числов А: "))
number_b = int(input("Введите степень числа B: "))
i = 0
total = 0
extetion = step_in(number_a, number_b)
print(f"{number_a} в степени {number_b} будет {extetion}")
