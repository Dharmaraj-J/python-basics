# Program For Armstrong Number
# THe Logic of The Program Is
    # xyz...=x^n+y^n+z^n....
    #  Where n is an order



def armstrong(num):

    length = len(str(num))

    sum =0
    temp = num

    while temp > 0:
        digits = temp % 10
        sum+=digits**length
        temp //=10


    if num == sum:
        print(f'the given number({num}) is armstrong number')

    else:
        print("It is not an armstrong number")    


num = int(input('Enter The Number :'))
armstrong(num)



