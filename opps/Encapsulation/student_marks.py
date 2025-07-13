class Student:
    def __init__(self, marks):
        self.__marks = marks  # private variable

    def set_marks(self,m):
        self.__marks = m    # set to given value

    def get_marks(self):
        return self.__marks  # return current marks

s1 = Student(4)

# Get and print initial marks
print("Initial Marks:", s1.get_marks())  # Output: 4

# Set new marks to 5 using setter method
s1.set_marks(6)

# Get and print updated marks
print("Updated Marks:", s1.get_marks())  # Output: 6    