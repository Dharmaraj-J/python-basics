class decorators:

    def __init__(self,ref):
        self.call = ref


    def __call__(self,*args):
        return self.call(*args).upper()

@decorators
def myfunc(str1,str2):
    return f'hello {str1} and {str2}'

print(myfunc('hari','siva'))


# obj = decorators(myfunc)
# print(obj('hari', 'siva'))