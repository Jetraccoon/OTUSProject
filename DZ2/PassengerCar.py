from Car import Car

class PassengerCar(Car):

    def __init__(self, weight, lifting, trunk_volume, engine):
        self.weight = weight
        self.lifting = lifting
        self.trunk_volume = trunk_volume
        self.engine = engine

    number_of_seats = 5
    gas_tank = 100
    fuel = 0

    def open_doors(self):
        print("doors open")

    def make_sound(self):
        print("Beep! Beep!")

    def tank_up(self, fuel):
        try:
            if self.fuel + fuel > self.gas_tank:
                raise ValueError
            self.fuel += fuel
        except ValueError:
            self.fuel = 100
            print("Gas tank is full")

    def start(self):
        try:
            if self.fuel <= 0:
                raise ValueError
            else:
                self.engine.start_engine()
        except:
            print("Fuel is down!")
