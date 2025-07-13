from abc import ABC, abstractmethod

class Polygon(ABC):

    @abstractmethod
    def sides(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def figure(self):
        return "This is 2D figure"

class Triangle(Polygon):

    def sides(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        return 0.5 * self.a * self.b
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def extra(self):
        return "this is a Triangle"

class Reactangle(Polygon):

    def sides(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
    def extra(self):
        return "this is a Rectangle"

class Square(Polygon):

    def sides(self, side):
        self.side = side

    def area (self):
        return self.side * self.side
    
    def perimeter(self):
        return 4 * self.side
    
    def extra(self):
        return "this is a Square"

t = Triangle()
t.sides(5, 10,3)       
      

r = Reactangle()
r.sides(2,5)


s = Square()
s.sides(4)

for obj in [t, r, s]:
    print(f"Type: {obj.extra()}")
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
    print(f"visibility: {obj.figure()}")



