class Vehicle:
    number_of_seats = 25

    def __init__(self, model):
        self.model = model

    def display(self):
        print(f"Vehicle model is '{self.model}' and it has '{self.number_of_seats}' seats.")


class Bus(Vehicle):
    pass


bus1 = Bus("Mercedes Benz Bus")
bus1.display()
