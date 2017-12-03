from enum import Enum


INPUT = 347991


class Direction(Enum):
    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3


def get_next_position(x, y, direction):
    if direction == Direction.RIGHT:
        return x + 1, y
    elif direction == Direction.UP:
        return x, y + 1
    elif direction == Direction.LEFT:
        return x - 1, y
    else:
        return x, y - 1


def get_spiral_positions():
    size = 0
    position = (0, 0)

    yield position
    while True:
        for direction in Direction:
            if direction in (Direction.RIGHT, Direction.LEFT):
                size += 1
            for i in range(size):
                position = get_next_position(*position, direction)
                yield position


def part_1(n):
    positions = get_spiral_positions()

    x = y = 0
    for _ in range(n):
        x, y = next(positions)

    return abs(x) + abs(y)


def get_neighbours(x, y):
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            yield i, j


def get_value(x, y, values):
    s = 0
    for pos in get_neighbours(x, y):
        s += values.get(pos, 0)
    return s


def part_2(n):
    values = {
        (0, 0): 1
    }

    for position in get_spiral_positions():
        value = sum([
            values.get(pos, 0)
            for pos in get_neighbours(*position)
        ])

        if value > n:
            return value
        values[position] = value


if __name__ == "__main__":
    print(f"Part 1: {part_1(INPUT)}")
    print(f"Part 2: {part_2(INPUT)}")
