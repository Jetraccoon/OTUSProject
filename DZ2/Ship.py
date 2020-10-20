from Transport import Transport

class Ship(Transport):

    def __init__(self, weight, lifting, displacement):
        self.weight = weight
        self.lifting = lifting
        self.displacement = displacement

    def make_sound(self):
        print("HOOOOORN!")
