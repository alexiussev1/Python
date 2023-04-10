import os
os.system('cls')

# просто о функциях:
def f(x):
    return x**2


print(f(2))
print(type(f))
print(type(f(2)))

a = f           #Теперь в контексте этого приложения a может использоваться точно так же, как и f
                #a — это переменная, которая хранит в себе ссылку на функцию.
print(a(2))
print(type(a))
print(type(a(2)))


def calc1(x):
    return x + x

def calc2(x):
    return x * x

def math(op, x):
    print(op(x))

math(calc1, 5)