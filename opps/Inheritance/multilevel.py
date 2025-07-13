# Multilevel inheritance is:

# A type of inheritance where a class is derived from a child class, which is already derived from another class.

class Grandparent:
    def gp(self):
        print("Hello from Grandparent")

class Parent(Grandparent):
    def p(self):
        print("Hello from Parent")

class Child(Parent):
    def c(self):
        print("Hello from Child")

c = Child()
c.gp()
c.p()
c.c()                



# class Vehicle:
#     def run(self):  # Grandparent class 
#         print("Vehicle is running")

# class Car(Vehicle):   # Parent class 
#     def drive(self):
#         print("Car is driving")

# class SportsCar(Car):  # Child class
#     def speed(self):
#         print("Sports Car is speeding")      

# s1 = SportsCar()
# s1.run()

# s1.drive()

# s1.speed()