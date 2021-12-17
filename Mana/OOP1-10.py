# Q1, Q4, Q5, Q6:

class Vehicle:

    def __init__(self, brand, color, max_speed, number_of_seats):
        self.brand = brand
        self.color = color
        self.max_speed = max_speed
        self.number_of_seats = number_of_seats

    def get_vehicle_specifications(self):
        return f"Brand: {self.brand}\nColor: {self.color}\nMax speed: {self.max_speed}"

    @staticmethod
    def miles_to_kilometers(self):
        return self.max_speed * 1.6093

    def brand_number_of_seats(self):
        return f"{self.brand}: {self.number_of_seats} seats"

class Bus(Vehicle):
    pass

# tiba = Vehicle("Saipa", "White", 149)
# print(tiba.get_vehicle_specifications())
# print(tiba.brand, tiba.color, tiba.max_speed)
# print(tiba.miles_to_kilometers())

# -----------------------------------------------------

# Q2:

class Vehicle:
    
    def __init__(self):
        pass

# -----------------------------------------------------

# Q3:

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Baaark"

# poppy = Dog("Poppy", 2)
# print(poppy.bark())

# ------------------------------------------------------

# Q7:

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"Name is: {self.name}\nAge is: {int(self.age)}"

class student(Person):

    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def display_student(self):
        return f"Name is: {self.name}\nAge is: {int(self.age)}\nSection is: {self.section}"

    
# person = Person("Mana", "24")
# student = student("Anna", "41", 2)
# print(student.display_student())

# ---------------------------------------------------------

# Q8:

class Rectangle:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def area(self):
        return self.width * self.length

    def display(self):
        return f"Width: {self.width} \nLength: {self.length} \nPerimeter: {self.perimeter()} \nArea: {self.area()}"

# ---------------------------------------------------------

# Q9:

class BankAccount:

    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, value):
        self.balance += value

    def withdrawal(self, value):
        self.balance -= value

    def bank_fees(self):
        self.balance -= (self.balance * 0.05)

    def display(self):
        return f"Account details:\nAccount number: {self.account_number}\nName: {self.name}\nBalance: {self.balance}"

# p1 = BankAccount(25, "saman", 100)
# p1.bank_fees()
# print(p1.balance)
# print(p1.display())

# --------------------------------------------------------

# Q10:

class Flashcard:

    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):     

        return f"{self.word} : {self.meaning}"

flash = []

while True:
    word = input("Enter your word [If you wanna end it press E/e]")
    if word == "e" or word == "E":
        break
    meaning = input("What is the meaning?")
    flash.append(Flashcard(word, meaning))

for item in flash:
    print(item)
