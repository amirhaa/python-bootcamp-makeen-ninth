class Vehicle:
    def __init__(self,brand,color,max_speed) :
        self.barnd = brand
        self.color = color
        self.max_speed = max_speed
    def conv_mile_to_km(self):
        Kmh =self.max_speed / 1.6
        return Kmh


motor = Vehicle("Harley","black",160)

print(motor.conv_mile_to_km())
