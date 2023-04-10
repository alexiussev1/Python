def fib(numb):
    if numb == 1 or numb ==0:
        return 1
    return fib(numb-1) + fib(numb - 2)

print (fib(10))
