from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


class Transport(metaclass=ABCMeta):
    weight: int
    lifting: int

    @abstractmethod
    def make_sound(self):
        pass


class Car(Transport):

    def __init__(self, weight, lifting):
        self.weight = weight
        self.lifting = lifting

    wheels = 4

    def make_sound(self):
        print("BEEEEEP!")


class Ship(Transport):

    def __init__(self, weight, lifting, displacement):
        self.weight = weight
        self.lifting = lifting
        self.displacement = displacement

    def make_sound(self):
        print("HOOOOORN!")


class Aircraft(Transport):

    def __init__(self, weight, lifting, ceiling):
        self.weight = weight
        self.lifting = lifting
        self.ceiling = ceiling

    def make_sound(self):
        print("TUUUUUT!")


class Passenger_Car(Car):

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


@dataclass
class Engine:
    capacity: int
    power: int
    count_pistons: int

    def start_engine(self):
        print("Engine started!")
