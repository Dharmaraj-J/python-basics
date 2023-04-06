# Program Name:Factorial of Number


def factorial(num):
    fact = 1

# Logic Of the Program

    if num < 0:
        print('Sorry, factorial does not exist for negative numbers')

        
    elif num == 0:
        print('the factorial of 0 is 1')    


    else:
        for i in range(1,num+1):
            fact = fact*i

        print("The factorial of",num,"is",fact)     


# Get The User Input
num = int(input('Enter the Number: '))
# Functon Call
factorial(num)





