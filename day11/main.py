ORIGIN = 0, 0


def read_input():
    return open('input.txt').read().rstrip().split(',')


def move(x, y, direction):
    if direction == 'n':
        return x, y - 1
    if direction == 's':
        return x, y + 1

    north_offset = (-1 if (x % 2 == 0) else 0)
    south_offset = (1 if (x % 2 == 1) else 0)

    if direction == 'ne':
        return x + 1, y + north_offset
    if direction == 'nw':
        return x - 1, y + north_offset

    if direction == 'se':
        return x + 1, y + south_offset
    if direction == 'sw':
        return x - 1, y + south_offset

    raise ValueError(direction)


def distance(x1, y1, x2, y2):
    x_distance = abs(x2 - x1)
    y_distance = max(abs(y2 - y1) - int(x_distance / 2), 0)
    return x_distance + y_distance


def part_1(directions):
    pos = ORIGIN

    for direction in directions:
        pos = move(*pos, direction)

    return distance(*ORIGIN, *pos)


def part_2(directions):
    pos = ORIGIN
    max_dist = 0

    for direction in directions:
        pos = move(*pos, direction)
        max_dist = max(max_dist, distance(*ORIGIN, *pos))

    return max_dist


if __name__ == '__main__':
    directions_input = read_input()

    print(f"Part 1: {part_1(directions_input)}")
    print(f"Part 2: {part_2(directions_input)}")
