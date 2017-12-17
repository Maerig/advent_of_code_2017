INPUT = 337


def part_1(step):
    values = [0]
    pos = 0

    for i in range(1, 2017 + 1):
        pos = (pos + step) % i + 1
        values.insert(pos, i)

    idx = values.index(2017)
    return values[idx + 1]


def part_2(step):
    pos = 0
    last_inserted = None

    for i in range(1, 50000000 + 1):
        pos = (pos + step) % i + 1
        if pos == 1:
            last_inserted = i

    return last_inserted


if __name__ == '__main__':
    print(f"Part 1: {part_1(INPUT)}")
    print(f"Part 2: {part_2(INPUT)}")