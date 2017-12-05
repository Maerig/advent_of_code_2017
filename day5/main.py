def read_input():
    return [
        int(line.rstrip())
        for line in open('input.txt').readlines()
    ]


def run_instructions(instructions, post_process):
    ip = 0
    steps = 0
    max_ip = len(instructions)

    while 0 <= ip < max_ip:
        delta = instructions[ip]
        instructions[ip] = post_process(instructions[ip])
        ip += delta
        steps += 1

    return steps


def part_1(instructions):
    return run_instructions(instructions, lambda n: n + 1)


def part_2(instructions):
    return run_instructions(instructions, lambda n: n + (-1 if n >= 3 else 1))


if __name__ == '__main__':
    print(f"Part 1: {part_1(read_input())}")
    print(f"Part 2: {part_2(read_input())}")
