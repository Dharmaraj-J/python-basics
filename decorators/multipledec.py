# Firstly the inner decorator will work and then the outer decorator work


def decor2(func):
    def inner():
        x = func()
        return x * x
    return inner
 
def decor1(func):
    def inner():
        x = func()
        return 2 * x
    return inner
 
@decor2
@decor1
def num():
    return 10
 
print(num())


