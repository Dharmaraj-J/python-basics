# factorial of number using recursion

def fact(n):
   
   if n<=1:
      return 1
   else:
      return n*fact(n-1)
   

number = int(input('enter the number: '))

if number<0:
   print('enter a positive number')
else:
   print(fact(number)) 