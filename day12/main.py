import re

from day12.program import Program

PROGRAM_COUNT = 2000
PROGRAM_REGEX = re.compile("(\d+) <-> (.*)")


def read_input():
    programs = [
        Program(i)
        for i in range(PROGRAM_COUNT)
    ]

    for line in open('input.txt'):
        number, piped_programs = PROGRAM_REGEX.match(line.rstrip()).groups()
        program = programs[int(number)]
        for piped in piped_programs.split(','):
            piped_program = programs[int(piped.strip())]
            program.add_piped(piped_program)

    return programs


def get_cluster(programs, number):
    return [
        program
        for program in programs
        if program.can_communicate_with(number)
    ]


def part_1(programs):
    cluster = get_cluster(programs, 0)
    return len(cluster)


def part_2(programs):
    cluster_count = 0

    while programs:
        for program in get_cluster(programs, programs[0].number):
            programs.remove(program)
        cluster_count += 1

    return cluster_count


if __name__ == '__main__':
    programs_input = read_input()

    print(f"Part 1: {part_1(programs_input)}")
    print(f"Part 2: {part_2(programs_input)}")
