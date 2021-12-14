class Vehicle:
    def __init__(self, brand, color, max_speed_mile):
        self.brand = brand
        self.color = color
        self.max__speed = max_speed_mile

    @staticmethod
    def mile_to_km(max_speed_km):
        print(max_speed_km * 1.6)


peugeot405 = Vehicle("IKco", "white", 240)
peugeot405.mile_to_km(peugeot405.max__speed)
