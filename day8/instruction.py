import re


from day8.condition import Condition
from day8.operation import Operation


class Instruction(object):
    REGEX = re.compile("(\w+) (\w+) (-?\d+) if (\w+) ([!<>=]+) (-?\d+)")

    def __init__(self, raw_instruction):
        groups = self.REGEX.match(raw_instruction).groups()
        self.operation = Operation(*groups[:3])
        self.condition = Condition(*groups[3:])

    def execute(self, registers):
        if self.condition.is_valid(registers):
            registers = self.operation.apply(registers)
        return registers
