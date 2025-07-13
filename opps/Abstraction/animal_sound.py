from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        return "Bark"
    
    def name(self):
        return "Dog"
    
class Cat(Animal):

    def sound(self):
        return "Meow"
    
    def name(self):
        return "Cat"

class Cow(Animal):

    def sound(self):
        return "Moo" 

    def name(self):
        return "Cow"    

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(f"{animal.name()} makes sound: {animal.sound()}")
       

