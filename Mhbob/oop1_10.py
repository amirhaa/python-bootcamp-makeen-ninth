# 1

class vehicle:
    def __init__(self, brand, color, max_speed):
        self.brand = brand
        self.color = color
        self.max_speed = max_speed

    def show_full_specs(self):
        return f'{self.brand} , {self.color} , {self.max_speed}'


car = vehicle('benz', 'whit', 280)

print(car.show_full_specs())

print('------------------------------------------------')
# 2

class vehicle:
    def user_specs(self, number_of_doors, name, color):
        self.number_of_doors = number_of_doors
        self.name = name
        self.color = color

        return f'{self.number_of_doors} & {self.name} & {self.color}'

specs = (4, 'bmw', 'black')
print(specs)

print('------------------------------------------------')
# 3

class dog:

    def __init__(self, name, age, pars_type):
        self.name = name
        self.age = age
        self.pars_type = pars_type

    def specs(self):
        return f'name is {self.name} and {self.age}  years old and pars type {self.pars_type}'

result = dog ('husky' , 6, 'haaaap')
print(result.specs())

print('------------------------------------------------')
# 4

print('------------------------------------------------')
# 5

class car :
    def __init__(self , name, mileage):
        self.name = name
        self.mileage = mileage

    def max_speed(self, speed):
        return f'the {self.name} runs at the maximum of {speed} km/hr'

honda = car ('honda', 21.5)
print(honda.max_speed(150))

print('------------------------------------------------')
# 6

class vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class bus(vehicle):
    def __init__(self, name):
        super().__init__(name = bus)
        return f'{self.name} ,  {self.mileage} , {self.capacity}'
        


school_bus =bus('school value', 12, 50)
print(school_bus())

print('--------------------------------------------')
# 7

class person :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def disply(self):
        print('person name : ', self.name)
        print('person age : ', self.age)


class student(person):
    def __init__(self, name, age, section):
        person.__init__(self, name, age)
        self.section = section

    def disply_student(self):
        print('student name : ', self.name)
        print('student age : ' , self.age)
        print('student section :', self.section)


person = disply('mobin', 29)
print(person.disply())

stu = disply_student('maxi', 20)
print(disply_student.stu)

print('----------------------------------------------------')
# 8
