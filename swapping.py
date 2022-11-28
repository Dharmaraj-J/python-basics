a=int(input("enter a value"))
b=int(input("enter b value"))


#swapping with third variable

temp = a
a = b
b = temp
print("swapping with third variable",a,b)

#swapping without using third variable

# 1. using bitwise operator

a = a^b
b = a^b
a = a^b

print("swapping without using third variable in bitwise operator",a,b)

# 2. using arithmetic operator
a = a+b
b = a-b
a = a-b

print("swapping without using third variable in arithmetic operator",a,b)




