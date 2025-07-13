# Protecting data by keeping it private and accessing it via methods.

# types 1. public , 2. protected, 3. private


# Define a class named Person
class Person:
    def __init__(self):
        self.__name = "vasu"  # private variable (name mangled as _Person__name)
        self.age = 23         # public variable

    # Public method to access the private variable __name
    def get_name(self):
        return self.__name    

# Create an object of the Person class
p = Person()

# Accessing the private variable using the public getter method
print(p.get_name())    # Output: vasu

# Accessing the public variable directly
print(p.age)           # Output: 23

# Attempting to access the private variable directly from outside the class
print(p.__name)        # ❌ This will raise an AttributeError
# Reason: __name is private and is name-mangled to _Person__name internally
