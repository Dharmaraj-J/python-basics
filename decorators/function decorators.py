

def uppercase(func):

    def procedure():

        data = func()
        return  data.upper()
    return procedure

@uppercase
def myfunction():
    return "hello welcom to pycharm"

print(myfunction())

 # result = uppercase(myfunction)
 # print(result())

