class SqrArea:
    def __init__(self,l=None):
        if l is None:
            self.length=eval(input('Enter the length: '))
        else:
            self.length=l
        print('Object SqrArea has created ')
    def cal_area(self):
        return self.length*self.length
    def __del__(self):
        print('Object has been destructed')
class SqrPeri:
    def __init__(self,l=None):
        if l is None:
            self.length=eval(input('Enter the length: '))
        else:
            self.length=l
        print('Object SqrPeri has created ') 
    def calc_area(self):
        return 4*self.length
    def __del__(self):
        print('Object has been destructed')           
class Square(SqrArea,SqrPeri):
    def __init__(self,l=None):
        if l is None:
            super().__init__()
        else:
            super().__init__(l)
        print('Object Square has created ')
    def Show(self):
        return super().calc_area(),super().cal_area()
    def __del__(self):
       print('Object has been destructed')             
f=eval(input('Enter the length:'))
a=SqrArea(f)
print('Area of square is ',a.cal_area())
b=SqrPeri(f)
print('Peripheral of square is ',b.calc_area())
d=Square(f)
print(d.Show())