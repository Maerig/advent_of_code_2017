from collections import defaultdict

from day8.instruction import Instruction


def read_input():
    return [
        Instruction(raw_instruction)
        for raw_instruction in open('input.txt').readlines()
    ]


def part_1(instructions):
    registers = defaultdict(int)

    for instruction in instructions:
        registers = instruction.execute(registers)

    return max(registers.values())


def part_2(instructions):
    registers = defaultdict(int)
    register_values = set()

    for instruction in instructions:
        registers = instruction.execute(registers)
        register_values = register_values.union(registers.values())

    return max(register_values)


if __name__ == '__main__':
    instructions_input = read_input()

    print(f"Part 1: {part_1(instructions_input)}")
    print(f"Part 2: {part_2(instructions_input)}")
