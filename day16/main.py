def read_input():
    return [
        instruction
        for instruction in open('input.txt').read().split(',')
    ]


def get_programs_input():
    return list("abcdefghijklmnop")


def run_instruction(instruction, programs):
    program_count = len(programs)

    if instruction[0] == 's':
        delta = int(instruction[1:])

        return [
            programs[(i - delta) % program_count]
            for i in range(program_count)
        ]

    if instruction[0] == 'x':
        x, y = [
            int(n)
            for n in instruction[1:].split('/')
        ]

        tmp = programs[x]
        programs[x] = programs[y]
        programs[y] = tmp

        return programs

    if instruction[0] == 'p':
        a, b = [
            x
            for x in instruction[1:].split('/')
        ]

        i = programs.index(a)
        j = programs.index(b)
        programs[i] = b
        programs[j] = a

        return programs


def run_instructions(instructions, programs):
    for instruction in instructions:
        programs = run_instruction(instruction, programs)

    return programs


def part_1(instructions, programs):
    return ''.join(run_instructions(instructions, programs))


def part_2(instructions, programs):
    # Get loop size
    loop_start = list(programs)
    loop_size = 0
    while programs != loop_start or loop_size == 0:
        programs = run_instructions(instructions, programs)
        loop_size += 1

    for i in range(1_000_000_000 % loop_size):
        programs = run_instructions(instructions, programs)

    return ''.join(programs)


if __name__ == '__main__':
    instructions_input = read_input()

    print(f"Part 1: {part_1(instructions_input, get_programs_input())}")
    print(f"Part 2: {part_2(instructions_input, get_programs_input())}")
