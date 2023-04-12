class A:
    def __init__(self):
        print('init A')
        
    def data1(self):
        print('data1')


    def data2(self):
        print('data2')

class B:
    
    def collection1(self):
        print('collection1')

    def collection2(self):
        print('collection2')

class C(B,A):
    def datacollection(self):
        print('datacollection')
        

c1 = C()
c1.datacollection()