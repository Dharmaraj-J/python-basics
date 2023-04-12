a = int(input('enter a  value : '))
b = int(input('enter b value : '))


try:
    c = a/b
    print(c)
    d= int(input('enter d value : '))
    print(c+d)

except ZeroDivisionError as e:
    print(e,'error')

except ValueError as e:
    print('Invalid Value')

except Exception as e:
    print(e)

finally:
    print('program run successfully')    
