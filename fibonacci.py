# Program to find Fibonacci Sequence

# Logic of fibonacci Sequece :
    #   Add the precedence of two numbers
    # 0,1,1,2,3,5,8....
    # The nth term is n-2+n-1

# While loop

def fibonacci(nterms):

    n1,n2 = 0,1
    count = 0

    if nterms <= 0:
        print('Enter a positive values')

    elif nterms == 1:
        print("the fibonacci sequence of ",nterms,"is:")
        print(n1)  

    else:
        print("fibononacci sequence is :")
        while(count < nterms):
            print(n1)
            nth = n1+n2
            n1 = n2
            n2 = nth
            count+=1
            
nterms = int(input('Enter How many Terms?'))
fibonacci(nterms)



# for loop

# def fibonacci(nterms):
    
#     n1,n2 = 0,1
    

#     if nterms <= 0:
#         print('Enter a positive values')

#     elif nterms == 1:
#         print("the fibonacci sequence of ",nterms,"is:")
#         print(n1)  

#     else:
#         print("fibononacci sequence is :")
#         for i in range(0,nterms):
#             print(n1)
#             nth = n1+n2
#             n1 = n2
#             n2 = nth
            
            
# nterms = int(input('Enter How many Terms?'))
# fibonacci(nterms)










