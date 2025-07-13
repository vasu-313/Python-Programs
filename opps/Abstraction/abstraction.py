# An abstractmethod in Python is a method declared in an abstract class that must be implemented by its subclasses.



from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def method1(self):
        pass

    def method2(self):
        print("this is concrete method")
    @abstractmethod
    def method3(self):
        pass    
class B(A):
    def method1(self):
        print("method1 is implemented in sub class")    
    def method3(self):
        print("method3 is implemented in sub class")    

b = B()
b.method1()        
b.method2()        
b.method3()        