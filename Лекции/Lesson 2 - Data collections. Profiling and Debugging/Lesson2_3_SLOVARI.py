# Словари — неупорядоченные коллекции произвольных объектов с доступом по ключу.
# В списках в качестве ключа используется индекс элемента. В словаре для определения
# элемента используется значение ключа (строка, число).
# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ← типы ключей могут отличаться
# print(dictionary['up']) # ↑ типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента

import os
os.system ('CLS')

d={}
d=dict()

d['q']='qwerty'
print(d)

d['w']='werty'
print(d['q'])

dictionary ={}
dictionary={'up':'↑','left':'←','down':'↓','right':'→'}
dictionary[895] = 98998
print(dictionary)

del dictionary['left'] # удаление элемента в словаре

for i in dictionary:
    print (i)

for i in dictionary:
    print ('{}: {}'.format(i, dictionary[i]))

for (k,v) in dictionary.items():
    print (k,v)

print (dictionary.items())
