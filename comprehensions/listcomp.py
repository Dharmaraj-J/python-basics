# syntax
# [expression for item in iterable if condition == True]


fruits = ['mango','apple','orange','kiwi']
newlist = [ i for i in fruits if 'a' in i] 
print(newlist)

#  lis contain 2000 values
list = [i for i in range(2000)]
# print(list)

# convert all the fruits in uppercase
 
upper = [i.upper() for i in fruits]
print(upper)