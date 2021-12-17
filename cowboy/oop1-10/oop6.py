class Vehicle:
    def __init__(self,brand,color,max_speed) :
        self.brand = brand
        self.color = color
        self.max_speed = max_speed

class Child_bus(Vehicle):
    pass

class Parent_vehicle(Vehicle):
    def __init__(self, brand, color, max_speed,num_seat):
        super().__init__(brand, color, max_speed)
        self.num_seat = num_seat
    def bd_ns(self):
        print(f"Model : {self.brand} , Number of seat : {self.num_seat}" )


p1 = Parent_vehicle("audi","red",260,4)

p1.bd_ns()
