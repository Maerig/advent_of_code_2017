class Condition(object):
    def __init__(self, register, operator, operand):
        self.register = register
        self.operator = operator
        self.operand = int(operand)

    def is_valid(self, registers):
        register_value = registers[self.register]

        if self.operator == '<':
            return register_value < self.operand
        elif self.operator == '<=':
            return register_value <= self.operand
        elif self.operator == '>=':
            return register_value >= self.operand
        elif self.operator == '>':
            return register_value > self.operand
        elif self.operator == '==':
            return register_value == self.operand
        elif self.operator == '!=':
            return register_value != self.operand