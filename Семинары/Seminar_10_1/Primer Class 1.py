import os
import random
os.system("cls")

class Human:
    name: str               # эти поля можно убрать
    ade: int                # эти поля можно убрать
    weght: int              # эти поля можно убрать
    height: float           # эти поля можно убрать

    # name:name - обозначение переменной....weght: float =100 - обозначение переменной со значением по умолчанию
    def __init__(self, name: str, age: int, weght: float = 100, height: float = 170):
        self.name = name
        self.age = age
        self.weght = weght
        self.height = height

    def hello(self):
        return f'Тебя приветствует {self.name}'


kirill = Human('Стоун', 38, height=210)
sveta = Human('Света', 18)

print(kirill.name)
print(kirill.height)
print(sveta.name)

print('*************')

print(kirill.hello())
print(sveta.hello())