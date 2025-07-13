# ✅ Benefits of Duck Typing:
# Flexible and dynamic

# Less boilerplate

# Supports polymorphism without inheritance

# Duck typing in Python is:

# "An object's behavior determines its usability, not its actual type."


class Manager:
    def get_bonus(self):
        return "Employee bonus: 10000"
    
class Developer:
    def get_bonus(self):
        return "Manager bonus: 20000"

# Duck typing function    

def show_bonus(employee):
    print(employee.get_bonus())

m1 = Manager()
d1 = Developer()

show_bonus(m1)
show_bonus(d1)

             

