class Particle(object):
    def __init__(self, position, velocity, acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def iterate(self):
        self.velocity += self.acceleration
        self.position += self.velocity
