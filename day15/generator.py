class Generator(object):
    MODULO_CONSTANT = 2147483647

    def __init__(self, factor, start):
        self.factor = factor
        self.start = start

    def get_values(self):
        n = self.start

        while True:
            n = (n * self.factor) % self.MODULO_CONSTANT
            yield n

    def get_multiple_values(self, multiple):
        n = self.start

        while True:
            n = (n * self.factor) % self.MODULO_CONSTANT
            if n % multiple == 0:
                yield n
