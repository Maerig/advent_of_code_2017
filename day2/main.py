def read_input():
    return [
        [
            int(i)
            for i in row.rstrip().split('\t')
        ]
        for row in open('input.txt')
    ]


def part_1(rows):
    s = 0
    for row in rows:
        s += max(row) - min(row)
    return s


def part_2(rows):
    s = 0
    for row in rows:
        for i, a in enumerate(row):
            for b in row[i + 1:]:
                if a % b == 0:
                    s += a // b
                elif b % a == 0:
                    s += b // a
    return s


if __name__ == "__main__":
    rows_input = read_input()

    print(f"Part 1: {part_1(rows_input)}")
    print(f"Part 2: {part_2(rows_input)}")
