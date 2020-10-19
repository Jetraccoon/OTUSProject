import oop

rb25 = oop.Engine(3.0,220,6)

nissan = oop.Passenger_Car(1000, 500, 300, rb25)
airbus = oop.Aircraft(10000, 2000, 4000)
ship = oop.Ship(20000, 6000, 2000)

nissan.start()
nissan.tank_up(120)
nissan.start()
nissan.make_sound()
nissan.open_doors()

airbus.make_sound()

ship.make_sound()
