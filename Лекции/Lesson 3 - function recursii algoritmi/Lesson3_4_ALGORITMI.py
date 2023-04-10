# Алгоритмом называется набор инструкций для выполнения
# некоторой задачи. В принципе, любой фрагмент
# программного кода можно назвать алгоритмом, но мы с
# Вами рассмотрим 2 самых интересных алгоритмы
# сортировок:
#        ● Быстрая сортировка
#        ● Сортировка слиянием

# Быстрая сортировка

# “Программирование это разбиение чего-то большого и невозможного на что-то
# маленькое и вполне реальное”
# Быстрая сортировка принадлежит такой стратегии, как “разделяй и властвуй”.
# Сначала рассмотрим пример, затем напишем программный код
# Два друга решили поиграть в игру: один загадывает число от 1 до 100, другой
# должен отгадать. Согласитесь, что мы можем перебирать эти значения в случайном
# порядке, например: 32, 27, 60, 73… Да, мы можем угадать в какой-то момент, но что
# если мы обратиться к стратегии “разделяй и властвуй” Обозначим друзей, друг_1
# это Иван, который загадал число, друг_2 это Петр, который отгадывает. Итак
# начнем:


import os
os.system("cls")


def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greator = [i for i in array[1:] if i > pivot]
    return quick_sort(less)+[pivot]+quick_sort(greator)


print(quick_sort([10, 5, 2]))


# Сортировка слиянием

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            nums[k] = right[j]
            j+=1
            k+=1
lest_1=[1,5,12,21,4512,123,123,123,5,56,65,54]
merge_sort(lest_1)
print(lest_1)