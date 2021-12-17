class Vehicle:
    def __init__(self,brand,color,max_speed) :
        self.barnd = brand
        self.color = color
        self.max_speed = max_speed


motor = Vehicle("Harley","black",160)

print(motor.__dict__)

        