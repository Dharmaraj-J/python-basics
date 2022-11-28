

def practice():
    s =  "practice makes"

    def hardwork():  # nested function
        h = " " "perfect"
        add = s+h
        return add
    return hardwork  #function return another function

obj = practice()
print(obj())  # function as a reference


