class Circle():
    def __init__(self,r = None):
        if r is None:
            self.radius = eval(input('Enter the radius of the circle: '))
        else:
            self.radius=r
        print('A circle has been created')
    def get_radius(self):
        return self.radius
    def calc_area(self):
        return 3.14*self.radius**2
    def __del__(self):
        print('Object has been destructed.')
