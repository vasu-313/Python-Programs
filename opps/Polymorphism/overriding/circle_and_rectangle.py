class Shape:
    def area(self):
        return "Area not defined for this shape"
    
class Circle(Shape):
    def area(self,radius):
        self.randius = radius
        area = 3.14 * radius * radius
        return f"Cicle Area: {area}"
    
class Rectangle(Shape):
    def area(self, length, width):
        self.length = length
        self.width = width
        area = length * width
        return f"Reactangle Area: {area}"
    
c1 = Circle()
print(c1.area(5))    

r1 = Rectangle()
print(r1.area(4,6))