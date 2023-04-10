# Множества содержат в себе уникальные элементы, не обязательно упорядочные.
# Одно множество может содержать значения любых типов. Если у вас есть два множества
# Вы можете совершать над ними любые стандартные операции, например объединение, пересечение и разность.

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok

import os
os.system('cls')

# add - добавление в множество значения
print("Функция add", "\n")
colors = {'red', 'green', 'blue'}
print(colors)
# так как значение было, то в множество оно не добавится - так как множестве уникальные значения
colors.add('red')
print(colors)
# так как значение было, то в множество оно не добавится - так как множестве уникальные значения
colors.add('gray')
print(colors)
print()

# remove - удаление из множества значения при наличии этого значения во множестве, при отсутсиви вывод ошибки

print("Функция remove", "\n")
colors = {'red', 'green', 'blue'}
print(colors)
colors.remove('green')
print(colors, "\n")

# discard - удаление из множества значения даже при остутсвии значения во множестве

print("Функция discord", "\n")
colors = {'red', 'green', 'blue'}
print(colors)

print("При отсутвии занчения во множестве", "\n")
colors.discard('yellow')
print(colors, "\n")

print("При присутствии занчения во множестве", "\n")
colors.discard('red')
print(colors, "\n")

# clear () - удаление всех элементов из множества - , будет пустое множество set()
print("Функция clear", "\n")
colors = {'red', 'green', 'blue'}
print(colors)
colors.clear()
print(colors)

# создание множества пустого set ()
q = set()
print()


# Операции со множествами в Python:

# Копирование множества copy
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
print('Копирования множества COPY')
c = a.copy()
print(a, c, '\n')

# Объединение множества - объединенное множесто будет содержать уникальные значения двух множеств union
print('Объединения множества UNION')
u = a.union(b)
print(a, '+', b, '=', u, '\n')

# Пересечения множеств - те элементы, которые есть в обоих множествах intersection
print('Пересечения множеств INTERSECTION')
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
i = a.intersection(b)
print(a, 'пересечение', b, '=', i, '\n')

# вычетание множеств - удалаются одинаковые элементы из множества , которые есть в другом множестве
print('Удаление из одного множества другого DIFFERENCE')
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
dl = a.difference(b)
print(a, '-', b, '=', dl, '\n')
dl = b.difference(a)
print(b, '-', a, '=', dl, '\n')

# сложные операции со множеством
# q=a.union(b).difference(a.intersection(b))
#       2           3            1              - порядок выполнения операции
#  объединение   удаление    пресечение
q = a.union(b).difference(a.intersection(b))
print(a, ' ', b, '=', q, '\n')

# Замороженное множество
a = {1, 2, 3, 5, 8}
b = frozenset(a)  # заморозили множеств, его никак не может изменять
print(b)
