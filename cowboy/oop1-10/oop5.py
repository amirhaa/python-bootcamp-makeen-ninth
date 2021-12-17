class Vehicle:
    def __init__(self,brand,color,max_speed) :
        self.barnd = brand
        self.color = color
        self.max_speed = max_speed

class Child_bus(Vehicle):
    pass


bus1 = Child_bus("benz","yellow",100)

print(bus1.barnd)