# ABSTRACTION
from abc import ABC,abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area():
        pass
    
class Circle(Shape):
    def area(self,radius=0):
        return pi*radius*radius
    
class Rectangle(Shape):
    def area(self,l=0,b=0):
        return l*b
    
circle=Circle()
rect=Rectangle()

print('Area of circle:',circle.area(2))
print('Area of rectangle:',rect.area(3,4))