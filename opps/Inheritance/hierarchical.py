# Hierarchical inheritance occurs when multiple child classes inherit from a single parent class.



class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

class Cow(Animal):
    def moo(self):
        print("Cow moos")


d = Dog()
c = Cat()
co = Cow() 


d.sound()
d.bark()

d.sound()
c.meow()


d.sound()
co.moo()


