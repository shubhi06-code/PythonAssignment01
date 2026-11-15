class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_vehicle(self):
        print("Brand:", self.brand)

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show_car(self):
        print("Model:", self.model)

class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def show_battery(self):
        print("Battery:", self.battery, "kWh")

car = ElectricCar("Tata", "Nexon EV", 40)
car.show_vehicle()
car.show_car()
car.show_battery()
