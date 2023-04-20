def gen():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    
# for values in gen():
    # print(values) 


# fibnocci series using generator


def fib(terms):
    a,b = 0,1

    while a < terms:
        yield a
        a,b = b,a+b

for i in fib(9):
    print(i)






