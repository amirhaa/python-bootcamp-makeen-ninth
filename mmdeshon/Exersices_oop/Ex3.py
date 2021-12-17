class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def bark():
        print("bark")


dog1 = Dog('tala', '4')
dog1.bark()
