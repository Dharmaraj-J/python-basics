# Syntax
# lambda arguments : expression

# Square
square = lambda a:a*a
# print(square(3))

# power
power = lambda a,b:a**b
# print(power(5,2))


def myfun(n):
    return lambda a:a*n

double = myfun(2)
triple = myfun(3)
# print(double(3))
# print(triple(11))

list1 = [3,5,3,2,4,67,7,543,22]
evens = list(filter(lambda n:n%2==0,list1))
print(evens)