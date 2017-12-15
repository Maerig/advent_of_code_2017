from day15.generator import Generator


FACTOR_A = 16807
FACTOR_B = 48271

START_A = 873
START_B = 583


def count_matches(values_a, values_b, value_count):
    match_count = 0

    for _ in range(value_count):
        if (next(values_a) & 0xffff) == (next(values_b) & 0xffff):
            match_count += 1

    return match_count


def part_1(a, b):
    return count_matches(
        a.get_values(),
        b.get_values(),
        40000000
    )


def part_2(a, b):
    return count_matches(
        a.get_multiple_values(4),
        b.get_multiple_values(8),
        5000000
    )


if __name__ == '__main__':
    generator_a = Generator(factor=FACTOR_A, start=START_A)
    generator_b = Generator(factor=FACTOR_B, start=START_B)

    print(f"Part 1: {part_1(generator_a, generator_b)}")
    print(f"Part 2: {part_2(generator_a, generator_b)}")
