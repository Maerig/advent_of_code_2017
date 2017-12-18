from day18.program import Program


def read_input():
    return [
        line.rstrip()
        for line in open('input.txt').readlines()
    ]


def part_1(instructions):
    p = Program(instructions)
    return p.run_until_block()[-1]


def part_2(instructions):
    p0 = Program(instructions, p=0)
    p1 = Program(instructions, p=1)

    sent_count = 0
    while True:
        p1.queue += p0.run_until_block()

        sent_list = p1.run_until_block()

        if not sent_list:
            return sent_count

        sent_count += len(sent_list)
        p0.queue += sent_list


if __name__ == '__main__':
    instructions_input = read_input()

    print(f"Part 1: {part_1(instructions_input)}")
    print(f"Part 2: {part_2(instructions_input)}")
