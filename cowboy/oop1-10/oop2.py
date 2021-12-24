class Vehicle:
    def __init__(self,brand,color,max_speed,price) :
        self.barnd = brand
        self.color = color
        self.max_speed = max_speed
        self.price = price
    def speed(self):
        print(f"{self.max_speed} +- 5 Km/H")
    def market_price(self):
        print(f"Price : {self.price} $ --- In Black friday 7% Off ---> Price : {int(self.price) *0.93} $ ")

motor = Vehicle("Harley","black",160,"37000")

motor.speed()
motor.market_price()