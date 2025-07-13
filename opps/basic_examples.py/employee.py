from types import MethodType

class Employee:
    A = 10
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def getEmployeeName(self):
        print(self.name)

    def getClassVariable(self):
        print(self.A)

    def updateEmployeeName(self, new_name):
        self.name = new_name
        

    def updateClassVariable(self, new_value):
        self.__class__.A = new_value

    def deleteInstanceVariable(self):
        del self.name

    def deleteClassvariable(self):
        del self.__class__.A   

emp1 = Employee("John", 101, "50K")
emp2 = Employee("anudeep", 102, "70K")

# emp1.getEmployeeName()
# emp1.updateEmployeeName("Vasu")
# emp1.getEmployeeName()
# emp1.getClassVariable()
# emp1.updateClassVariable(200)
# print(Employee.A)


# emp1.deleteClassvariable()
# print(Employee.A)

# emp1.deleteInstanceVariable()
# print(emp1.name)


def addingMethod(self):
    print("method added successfully from outside")

emp1.newInstanceMethod = MethodType(addingMethod, emp1)    

emp1.newInstanceMethod()

emp2.newInstanceMethod()

