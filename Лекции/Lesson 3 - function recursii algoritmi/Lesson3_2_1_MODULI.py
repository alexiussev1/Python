# Модульность

# Вы когда-нибудь задавались вопрос, как например работает функция .append
# Это же точно такая же функция, как и sumNumbers(n), но мы ее нигде не создаем,
# все дело в том что, это функция автоматически срабатывает и чтобы ей
# пользоваться ничего дополнительно писать не надо.
# Представьте себе такую ситуацию, что Вы создаете огромный проект и у Вас
# имеется большое количество функций, к примеру 5 функций работают со
# словарями, 18 со списками и тд. и у каждой функции свой алгоритм, но их
# объединяет работа с одной коллекцией данных. Согласитесь неудобно работать в
# таком большом файле, где около 80 функций, очень легко потеряться и на
# перемотку кода Вы будете терять драгоценное время. Решение данной проблемы
# есть. Давайте будем создавать отдельные файлы, где будут находиться только
# функции, и эти функции при необходимости вызывать из главного файла

import Lesson322modul
import os
os.system("cls")

print(Lesson322modul.max1(5, 9))


# импортируем функцию из модуля напрямую
from Lesson322modul import max1
print(max1(9, 5))

# импортируем все функции
from Lesson322modul import *
print(max1(9, 5))

# импортируем модуль как имя (переименовываем в рамках программы)
import Lesson322modul as m1
print(m1.max1(11, 12))