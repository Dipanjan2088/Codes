class StLine:
    def __init__(self,l=None):
        if l is None:
            self.length=eval(input('Enter the length: '))
        else:
            self.length=l
            print('A straight line has been created of length ',self.length)    
class Square(StLine):
    def __init__(self,l=None):
        if l is None:
            super().__init__()
        else:
            super().__init__(l)
            print('A Square has been created of length ',self.length)
    def calc_area(self):
        return self.length*self.length
class Cube(Square):
    def __init__(self,l=None):
        if l is None:
            super().__init__()
        else:
            super().__init__(l)
            print('A cube has been created of length',self.length)
    def calc_area(self):
        return 6*super().calc_area()

l=eval(input('Enter the length:'))
a=Cube(10)
b=Square(20)
c=StLine(l)
print('Total area of cube is ',a.calc_area())