class Person:
    def __init__(self,name,age) :
        self.name = str(name)
        self.age = str(age)
    def display(self):
        return self.name , self.age

class Student(Person):
    def __init__(self, name, age,section):
        super().__init__(name, age)
        self.section = section
    def displayStudents(self):
        return self.name , self.age , self.section


student_1 = Student("Mike",18,"whatever")

print(student_1.displayStudents())
