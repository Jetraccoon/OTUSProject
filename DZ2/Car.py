from Transport import Transport

class Car(Transport):

    def __init__(self, weight, lifting):
        self.weight = weight
        self.lifting = lifting

    wheels = 4

    def make_sound(self):
        print("BEEEEEP!")
