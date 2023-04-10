# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским
# алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка;
# K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.

# *Пример:*
# ноутбук
#     12
import os

os.system("cls")

dictionary_1 = {
    1: ['AEIOULNSTRАВЕИНОРСТ'],
    2: ["DGДКЛМПУ"],
    3: ['BCMPБГЁЬЯ'],
    4: ['FHVWYЙЫ'],
    5: ['KЖЗХЦЧ'],
    6: [''],
    7: [''],
    8: ['JXШЭЮ'],
    9: [''],
    10: ['QZФЩЪ']
}

input_word = input('Введите любое слово для оценки его стоимости:')
input_word = input_word.upper()
input_word = list(input_word)

price_of_word = int(0)

for i in range(len(input_word)):
    for j in range(1, 11):
        if input_word[i] in str(dictionary_1[j]):
            price_of_word=price_of_word+j
            break       
print("Стоимость слова: ", price_of_word)

# решаем пример на семинаре 5


my_dict = {
    1: ['AEIOULNSTRАВЕИНОРСТ'],
    2: ["DGДКЛМПУ"],
    3: ['BCMPБГЁЬЯ'],
    4: ['FHVWYЙЫ'],
    5: ['KЖЗХЦЧ'],
    8: ['JXШЭЮ'],
    10: ['QZФЩЪ']
}


total = 0 
word = input ('Введите слово: ')
for letter in word:
    for key, value in my_dict.items():
        if letter.upper() in value:
            total+=key
print(f"Стоимость слова {total}")