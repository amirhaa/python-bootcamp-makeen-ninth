class Vehicle:
    def __init__(self, brand, color, max_speed_mile):
        self.brand = brand
        self.color = color
        self.max__speed = max_speed_mile

    @staticmethod
    def mile_to_km(max_speed_km):
        return max_speed_km * 1.6


class Bus(Vehicle):
    pass
