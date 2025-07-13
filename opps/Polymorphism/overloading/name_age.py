class Person:
    def display(self, name, age=None):
        self.name = name
        self.age = age
        if age is None:
            return f"Name: {self.name}"
        else:
            return f"Name: {self.name}, Age: {self.age}" 
        
p1 = Person()
print(p1.display("anudeep")) #Name: anudeep
print(p1.display("anudeep", 24))   #Name: anudeep, Age: 24      