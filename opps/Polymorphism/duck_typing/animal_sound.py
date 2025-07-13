class Duck:
    def sound(self):
        print("Quack")

class Dog:
    def sound(self):
        print("Woof")

class Cat:
    def sound(self):
        print("Meow")

def display_sound(obj):
    obj.sound()

d = Duck()
display_sound(d)    

do = Dog()
display_sound(do)  

c = Cat()
display_sound(c)  
