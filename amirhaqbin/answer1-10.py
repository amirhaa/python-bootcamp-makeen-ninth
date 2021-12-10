# Q1. Write a python programm that create a Vehicle class with brand, color and max_speed
# instance attributes. then create an instance and print the instance attribute\
# class vehicle:
#     def __init__(self, brand, color, max_speed):
#         self.brand = brand
#         self.color = color
#         self.max_speed = max_speed

#     def vehicle_specifications(self):
#         return f"Brand: {self.brand} , Color: {self.color} , Max speed: {self.max_speed}"


# land_crouse = vehicle('toyota', 'blue', 280)
# print(land_crouse.vehicle_specifications())


# Q2.Create a Vehicle class without any variables and methods
# class vehicle_2:
#     def __init__(self):
#         pass

# Q3. Create a Dog class that has name, age
# and an instance method that bark (when bark method is called print 'Bark')
# class dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def dog_specification(self):
#         return f"name : {self.name}\nage: {self.age}years"

#     def bark(self):
#         return "hap hap"


# sag = dog('jessi', '4')
# print(sag.dog_specification())
# print(sag.bark())


# Q4. Create a class Vehicle
# with attributes of the Q1 and also with a static method that converts Miles per hour to Kilometers per hour.
# class vehicle:
#     def __init__(self, brand, color, max_speed):
#         self.brand = brand
#         self.color = color
#         self.max_speed = max_speed

#     def vehicle_specifications(self):
#         return f"Brand: {self.brand} , Color: {self.color} , Max speed: {self.max_speed}MILE"
#     @staticmethod
#     def miles_to_kilometers(self):
#         return self.max_speed * 1.6093

# land_crouse = vehicle('toyota', 'blue', 280)
# print(land_crouse.vehicle_specifications())
# print(land_crouse.miles_to_kilometers())

# Q5. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class (in Q4)
# class Bus(Vehicle):
#     pass

# Q6. Create a parent class Vehicle and a child class Bus, parent class should have number of seats attribute
# and have a method that prints out the model of the car and number of seats.
# def brand_number_of_seats(self):
#         return f"{self.brand}: {self.number_of_seats} seats"

# Q7 Create a Python class Person with attributes: name and age of type string.
# Create a display() method that displays the name and age of an object created via the Person class.
# Create a child class Student  which inherits from the Person class and which also has a section attribute.
# Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
# Create a student object via an instantiation on the Student class and then test the displayStudent method.

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def person_display(self):
#         return f" name : {self.name} , age : {self.age}"
# class student(person):
#     def __init__(self, name, age, section):
#         super().__init__(name, age)
#         self.section = section
#     def student_display(self):
#         return f"student_name : {self.name}\n student_age: {self.age}\n section : {self.section}"
# student_1 = student('mike', 17 , 'highschool_student')
# print(student_1.student_display())


# Q8. Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
# Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.
# Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.

# class rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def perimeter(self):
#         return ((self.length)+(self.width)) * 2

#     def area(self):
#         return(self.length * self.width)


# rectangle_1 = rectangle(10, 20)
# print(rectangle_1.perimeter())
# print(rectangle_1.area())

# Q9. Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
# Create a constructor with parameters: accountNumber, name, balance.
# Create a Deposit() method which manages the deposit actions.
# Create a Withdrawal() method  which manages withdrawals actions.
# Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
# Create a display() method to display account details.

# class BankAccount:

#     def __init__(self, account_number, name, balance):
#         self.account_number = account_number
#         self.name = name
#         self.balance = balance

#     def deposit(self, value):
#         self.balance += value

#     def withdrawal(self, value):
#         self.balance -= value

#     def bank_fees(self):
#         self.balance -= (self.balance * 0.05)

#     def display(self):
#         return f"Account details:\nAccount number: {self.account_number}\nName: {self.name}\nBalance: {self.balance}"

# p1 = BankAccount(20, "melli", 1000)
# p1.bank_fees()
# print(p1.balance)
# print(p1.display()


# Q10. Create a flash card.
# Take the word and its meaning as input from the user.
# Create a class named flashcard, use the __init__() function to assign values for Word and Meaning.
# Now we use the __str__() function to return a string that contains the word and meaning.
# Store the returned strings in a list named flash.
# Use a while loop to print all the stored flashcards.

# class Flashcard:
    
    # def __init__(self, word, meaning):
    #     self.word = word
    #     self.meaning = meaning

    # def __str__(self):     

    #     return f"{self.word} : {self.meaning}"

