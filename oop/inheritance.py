class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    


class Square(Rectangle,Shape):
    def __init__(self,side):
        self.width = side
        self.height = side

        