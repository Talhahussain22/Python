#In this we change the method of parent class in child class:

class Shape():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y


class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(self.radius,self.radius)
    def area(self):
        return 3.14 * super().area()
c=Circle(10)
print(c.area())

rec=Shape(3,4)
print(rec.area())

