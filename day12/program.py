class Program(object):
    def __init__(self, number):
        self.number = number
        self.piped = set()

    def add_piped(self, program):
        self.piped.add(program)
        program.piped.add(self)

    def can_communicate_with(self, number, visited=None):
        if number == self.number:
            return True

        if not visited:
            visited = []

        for program in self.piped:
            if program not in visited and program.can_communicate_with(number, visited + [self]):
                return True

        return False
