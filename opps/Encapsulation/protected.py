# 2. Protected Encapsulation
# Definition: Members prefixed with _ are intended for access within the class and its subclasses.

class Demo:
    def __init__(self):
        self._name = "vasu" #protected

d = Demo()
print(d._name)