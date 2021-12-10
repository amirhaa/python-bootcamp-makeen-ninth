class Person:
    def __init__(self, name: str, age: str):
        self.name = name
        self.age = age

    def display(self):
        return f"his/her name is '{self.name}' and he/she is '{self.age}' years old."


class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def display_student(self):
        return f"'{self.name}' is '{self.age}' years old. section is '{self.section}'."


person1 = Person("ali", "24")
print(person1.display())

student1 = Student("naser", 24, 8)
print(type(student1.age))
print(student1.display_student())
