# sum of n numbers using recursion

def sum(n):
    if n==1:
        return n
    else:
       return sum(n-1) + n

number = int(input('enter the number :'))
print(sum(number))

