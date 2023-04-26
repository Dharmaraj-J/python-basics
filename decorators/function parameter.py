

def function1():
    return "function 1 is calling"

def function2(ref):
    print(ref())
    print("function 2 is calling")

function2(function1) # function as a parametre