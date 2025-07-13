class AreaCalculator:
    def area(self,a, b=None,):
        if b is None:
            return f"Circle Area: {3.14 * a * a}"
        elif isinstance(a, float) and isinstance(b, float):
            return f"Triange Area: {0.5 * a * b}"
        else:
            return f"Rectangle Area: {a * b}"

        
a1 = AreaCalculator()
print(a1.area(5))    # Circle Area 
print(a1.area(5.0, 10.0)) # Triangle Area    
print(a1.area(5, 10)) # Rectangle Area



        
