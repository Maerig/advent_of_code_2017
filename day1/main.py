def read_input():
    return open('input.txt').readline()


def get_number_pairs(numbers, offset):
    number_count = len(numbers)
    for i, n in enumerate(numbers):
        yield n, numbers[int((i + offset) % number_count)]


def sum_matching_pairs(pairs):
    return sum(
        int(x)
        for x, y in pairs
        if x == y
    )


def part_1(numbers):
    number_pairs = get_number_pairs(numbers, 1)
    return sum_matching_pairs(number_pairs)


def part_2(numbers):
    number_pairs = get_number_pairs(numbers, len(numbers) // 2)
    return sum_matching_pairs(number_pairs)


if __name__ == '__main__':
    numbers_input = read_input()

    print(f"Part 1: {part_1(numbers_input)}")
    print(f"Part 2: {part_2(numbers_input)}")
