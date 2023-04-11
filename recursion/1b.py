# fibonacci using recursion 


def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1) + fib(n-2)

number = int(input('Enter how many terms? :'))

if number<0:
    print('Enter positive terms')
else:    
    for i in range(number):
        print(fib(i))