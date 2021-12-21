class StLine:
    def __init__(self,l=None):
        if l is None:
            self.length=eval(input('Enter the length: '))
        else:
            self.length=l
            print('A straight line has been created of length ',self.length)    
class SqrArea(StLine):
    def __init__(self,l=None):
        if l is None:
            super().__init__()
        else:
            super().__init__(l)
            print('A Square has been created of length ',self.length)    
    def calc_area(self):
        return self.length*self.length
class SqrPeri(StLine):
    pass
l=eval(input('Enter the length:'))
a=SqrArea(l)
print('Total area of cube is ',a.calc_area())