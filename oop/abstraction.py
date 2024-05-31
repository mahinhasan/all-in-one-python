from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        print("Hello")
    
    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    


rec = Rectangle(2,2)
print(rec.area())