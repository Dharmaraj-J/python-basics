print("using normal method")
list = ["ram","manoj","mathava"]
first , second, third = list
print(first)
print(second)
print(third)
print('\n')

print('using for loop  ' )
for lists in list:
    print(lists)      # using for loop
print('\n')

print('usin while loop')
i = 0
while (i < len(list)):

    print(list[i])  # using while loop
    i=i+1

print('\n')
print('using enumerate method')
for index,letters in enumerate(list):
    print(letters,index)  # using enumerate method with index






