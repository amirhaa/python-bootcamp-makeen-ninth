#Q1
print('----------------------------------------------------------------\nQ1')

class Vehicle:
    def __init__(self, brand, color, max_speed):
        self.brand = brand
        self.color = color
        self.max_speed = max_speed

car1 = Vehicle('BMW', 'black', 240)
print(f'car1 is a {car1.color} {car1.brand} with maximum speed of {car1.max_speed} M/H .')


#Q2
print('----------------------------------------------------------------\nQ2')

class Vehicle:
    pass


#Q3
print('----------------------------------------------------------------\nQ3')

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('Baaaaaaaaark!!!')

dog1 = Dog('cooper', 3)
dog1.bark()


#Q4
print('----------------------------------------------------------------\nQ4')

class Vehicle:
    def __init__(self, brand, color, max_speed):
        self.brand = brand
        self.color = color
        self.max_speed = max_speed

    @staticmethod
    def mile_to_km(max_speed):
        return max_speed * 1.60934

car1 = Vehicle('Benz', 'white', 200)
print(f'car1 is a {car1.color} {car1.brand} with maximum speed of {Vehicle.mile_to_km(car1.max_speed)} KM/H .')


#Q5
print('----------------------------------------------------------------\nQ5')

class Bus(Vehicle):
    def __init__(self, brand, color, max_speed):
        super().__init__(brand, color, max_speed)

#Q6
print('----------------------------------------------------------------\nQ6')

class Vehicle:
    def __init__(self, brand, color, max_speed, number_of_seats):
        self.brand = brand
        self.color = color
        self.max_speed = max_speed
        self.number_of_seats = number_of_seats

    def get_info(self):
        print(f'The car model is {self.brand} and it has {self.number_of_seats} seats.')

class Bus(Vehicle):
    def __init__(self, brand, color, max_speed, number_of_seats):
        super().__init__(brand, color, max_speed, number_of_seats)

bus1 = Bus('Mack', 'green', 100, 20)
print(f'bus1 is a {bus1.color} {bus1.brand} with maximum speed of {bus1.max_speed} M/H which has {bus1.number_of_seats} seats.')


#Q7
print('----------------------------------------------------------------\nQ7')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f'name: {self.name}\tage: {self.age}')

class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def displayStudent(self):
        print(f'name: {self.name}\tage: {self.age}\t\tsection: {self.section}')

stu = Student('Ali', 21, 2)
stu.display()
stu.displayStudent()


#Q8
print('----------------------------------------------------------------\nQ8')

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def display(self):
        print(f'length: {self.length}\t\twidth: {self.width}\t\tperimeter: {self.perimeter()}\t\tarea: {self.area()}')

rec1 = Rectangle(5, 3)
rec1.display()


#Q9
print('----------------------------------------------------------------\nQ9')


class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print('Sorry, you don\'t have enough balance!')
        else:
            self.balance -= amount

    def bankFees(self):
        return self.balance * 5 / 100

    def display(self):
        print('Account info :\n')
        print(f'Owner\'s Name: {self.name}\nAccount Number: {self.accountNumber}\nBalance: {self.balance}\nBank Fees: {self.bankFees(): .2f}')

my_acc = BankAccount(1167, 'Ali Hosseinzadeh', 500000)
my_acc.deposit(250000)
my_acc.withdraw(100000)
my_acc.display()


#Q10
print('----------------------------------------------------------------\nQ10')

#approach 1
class Flashcard:
    def __init__(self, **dikt):
        self.dict = dikt
        
    def get_words(self):
        for word, meaning in self.dict.items():
            print(word + ': ' + meaning)

    @staticmethod
    def take_words():
        dictt = {}
        while True:
            word = input('Enter a word (or press 0 to exit): ')
            if word == '0':
                break
            meaning = input('Enter its meaning : ')
            dictt[word] = meaning
            print('----------------------') 
        return dictt


dictt = Flashcard.take_words()
f1 = Flashcard(**dictt)
f1.get_words()


# #approach 2
# class Flashcard:
#     def __init__(self, word, meaning):
#         self.flash_card = {}
#         self.flash_card[word] = meaning
#         # self.flash_card.update({word: meaning})

#     def get_words(self):
#         for word, meaning in self.flash_card.items():
#             print(word + ': ' + meaning)

# word, meaning = input('Enter a word and its meaning (sepreted by space): ').split()
# f1 = Flashcard(word, meaning)
# f1.get_words()