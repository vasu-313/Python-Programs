# Multiple inheritance is:

# A feature where a class inherits from more than one parent class.


class A:
    def display1(self):
        print("Class A")

class B:
    def display2(self):
        print("Class B")

class C(A, B):
    def display3(self):
        print("Class C")


c1 = C()
c1.display1()
c1.display2()
c1.display3()
                       