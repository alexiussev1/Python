# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

import random
numb_list = [random.randint(0, 20) for _ in range(40)]

print (numb_list)
print (type(numb_list))
my_set = set (numb_list)
print (my_set)
print (len(my_set))

# my_tuple = (1,2,3,4)
# _, _, с, _=my_tuple

