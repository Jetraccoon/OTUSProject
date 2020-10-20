from Transport import Engine
from PassengerCar import PassengerCar
from Aircraft import Aircraft
from Ship import Ship

if __name__ == "__main__":
    rb25 = Engine(3.0,220,6)
    nissan = PassengerCar(1000, 500, 300, rb25)
    airbus = Aircraft(10000, 2000, 4000)
    ship = Ship(20000, 6000, 2000)

    nissan.start()
    nissan.tank_up(120)
    nissan.start()
    nissan.make_sound()
    nissan.open_doors()
    airbus.make_sound()
    ship.make_sound()
