class Rectangle:
    rectangles_quantity = 0  

    def __init__(self, w, h):
        self.w = w  
        self.h = h  
        Rectangle.rectangles_quantity += 1

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

    def is_square(self):
        return self.w == self.h
r = Rectangle(5, 10)
print(r.area())       
print(r.perimeter())  
print(r.is_square())  
print(Rectangle.rectangles_quantity) 
