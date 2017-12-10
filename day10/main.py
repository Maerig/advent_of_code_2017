from functools import reduce

EXTRA_LENGTHS = [17, 31, 73, 47, 23]


def read_input():
    return open('input.txt').read().rstrip()


def get_lengths():
    return [
        ord(c)
        for c in open('input.txt').read().rstrip()
    ] + EXTRA_LENGTHS


def reverse(values, pos, length):
    new_values = list(values)
    for i in range(length):
        new_values[(pos + i) % len(values)] = values[(pos + length - i - 1) % len(values)]

    return new_values


def part_1(raw_lengths):
    values = list(range(256))
    current_pos = 0
    skip_size = 0

    lengths = [
        int(length)
        for length in raw_lengths.split(',')
    ]

    for length in lengths:
        values = reverse(values, current_pos, length)
        current_pos = (current_pos + length + skip_size) % len(values)
        skip_size += 1

    return values[0] * values[1]


def get_chunks(values, size):
    for i in range(0, len(values), size):
        yield values[i:i + size]


def part_2(raw_lengths):
    values = list(range(256))
    current_pos = 0
    skip_size = 0

    lengths = [
        ord(c)
        for c in raw_lengths
    ] + EXTRA_LENGTHS

    for _ in range(64):
        for length in lengths:
            values = reverse(values, current_pos, length)
            current_pos = (current_pos + length + skip_size) % len(values)
            skip_size += 1

    chunks = get_chunks(values, 16)
    dense_hash = [
        reduce(lambda x, y: x ^ y, chunk)
        for chunk in chunks
    ]

    return ''.join([
        "%02x" % n
        for n in dense_hash
    ])


if __name__ == '__main__':
    lengths_input = read_input()

    print(f"Part 1: {part_1(lengths_input)}")
    print(f"Part 2: {part_2(lengths_input)}")
