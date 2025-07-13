# Inheritance means one class (child) can use the properties and methods of another class (parent).

# ✅ 🔹 Structure of Inheritance in Python

# class Parent:
#     # parent class methods and attributes

# class Child(Parent):
#     # child inherits from parent
#     # can use or override parent methods


# ✅ 🔹 Types of Inheritance in Python

# Single	One child from one parent
# Multiple	One child from multiple parents
# Multilevel	Child → Parent → Grandparent
# Hierarchical	Multiple children from one parent
# Hybrid	Combination of the above types

# Single Inheritance Example

class Parent:
    def pgreet(self):
        print("Hello from Parent") 

class Child(Parent):
    def cgreet(self):
        print("Hello from Child")     

c1 = Child()
c1.pgreet()           
c1.cgreet()           