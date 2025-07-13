# Hybrid inheritance is a combination of two or more types of inheritance (like single, multiple, multilevel, hierarchical) in one program.
# ✅ Example: Hybrid Inheritance (Mix of Multilevel + Multiple)

class Person:
    def info(self):
        print("i am a person")

# Hierarchical inheritance
class Student(Person):
    def student_info(self):
        print("i am a student")

class Teacher(Person):
    def teacher_info(self):
        print("i am a teacher")

# Multiple Inheritance
class Principal(Student, Teacher):
    def principal_info(self):
        print("i am a principal") 

t = Principal()     

t.info()
t.student_info()
t.teacher_info()
t.principal_info()