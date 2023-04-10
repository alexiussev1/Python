# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

width_share = int(input ('Количество долек по большей стороне '))
height_share = int(input ('Количество долек по меньшей стороне '))
broken_share = int(input ('Введите количество долек одного разлома шоколадки '))

if (width_share==1 or height_share==1) and (broken_share<width_share):
    print ('Да, это возможно отломить за раз')
elif (width_share!=1 and height_share!=1) and (broken_share%width_share==0 or broken_share%height_share==0):
    print ('Да, это возможно отломить за раз')
else:
    print ('Нет, это невозможно отломить за раз')

# print (broken_share%width_share)
# print (broken_share%height_share)