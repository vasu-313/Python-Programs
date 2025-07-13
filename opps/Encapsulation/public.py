# 1. Public Encapsulation
# Definition: Members are accessible from anywhere.

class Demo:
    def __init__(self):
        self.name = "vasu"


d = Demo()
print(d.name)