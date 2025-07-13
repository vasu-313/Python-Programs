class AreaCalculator:
    def area(self, *args):
        if len(args) == 1:
            side = args[0]
            area = side * side 
            return f"Square Area: {area}"
        elif len(args) == 2:
            length, width = args
            area = length * width
            return f"Rectangle Area: {area}"
        else:
            raise ValueError("Provide 1 argument for square or 2 arguments for rectangle")
        
a1 = AreaCalculator()
print(a1.area(5))        
print(a1.area(2,4))        