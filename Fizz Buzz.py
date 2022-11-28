def Fizz_buzz(x):
    if ((x%3 == 0)and(x%5==0)) :
        return ("Fizz Buzz")
    elif x % 3 == 0:
        return ("Fizz")
    elif x%5 == 0:
        return("Buzz")
    else:
        return x


print(Fizz_buzz(15))



