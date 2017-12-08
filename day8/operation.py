class Operation(object):
    def __init__(self, register, operation_type, operand):
        self.register = register
        self.operation_type = operation_type
        self.operand = int(operand)

    def apply(self, registers):
        if self.operation_type == 'inc':
            registers[self.register] += self.operand
        elif self.operation_type == 'dec':
            registers[self.register] -= self.operand
        else:
            raise ValueError(self.operation_type)

        return registers
