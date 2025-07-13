class Calculator:

    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def sub(a, b):
        return a - b
    
    @staticmethod
    def mult(a, b):
        return a * b
    
    @staticmethod
    def div(a, b):
        return a // b
    

# c1 = Calculator()

# print(c1.add(4, 3))
# print(c1.sub(4, 3))         # calling using object 
# print(c1.mult(4, 3))
# print(c1.div(4, 3))


print(Calculator.add(3,5))
print(Calculator.sub(3,5))
print(Calculator.mult(3,5))      # calling using class name
print(Calculator.div(3,5))
