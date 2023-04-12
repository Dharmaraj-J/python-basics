class A:
    def feature1(self):
        print('future 1')

    def feature2(self):
        print('future 2')    
     
class B(A):

    def feature3(self):
        print('future 3')

    def feature4(self):
        print('future 4') 

class C(B):
    def feature5(self):
        print('future 5')
     


c1 = C()
c1.feature5()
