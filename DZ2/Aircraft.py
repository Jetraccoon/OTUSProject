from Transport import Transport

class Aircraft(Transport):

    def __init__(self, weight, lifting, ceiling):
        self.weight = weight
        self.lifting = lifting
        self.ceiling = ceiling

    def make_sound(self):
        print("TUUUUUT!")