class Animal:

    def sound(self):
        return "woof"    
    
class Dog(Animal):

    def sound(self):
        return "bark"   

class Cat(Animal):
    def sound(self):
        print("meows")     
    
a1 = Dog()  
print(a1.sound())  

a2 = Cat()  
a2.sound()