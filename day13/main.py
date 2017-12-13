from day13.scanner import Scanner


def read_input():
    return [
        line.rstrip()
        for line in open('input.txt')
    ]


def part_1(scanners):
    total_damage = 0

    for i, scanner in scanners.items():
        if scanner.get_position(i) == 0:
            total_damage += i * scanner.size

    return total_damage


def generates_damage(scanners, t):
    for i, scanner in scanners.items():
        if scanner.get_position(i + t) == 0:
            return True
    return False


def part_2(scanners):
    start_time = 0

    while generates_damage(scanners, start_time):
        start_time += 1

    return start_time


if __name__ == '__main__':
    raw_lines = read_input()
    scanners_input = Scanner.read_scanners(raw_lines)

    print(f"Part 1: {part_1(scanners_input)}")
    print(f"Part 2: {part_2(scanners_input)}")
