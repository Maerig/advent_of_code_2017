from utils.vector import Vector
from utils.progress import show_progress


DIRECTIONS = [
    Vector(0, -1),  # UP
    Vector(1, 0),   # RIGHT
    Vector(0, 1),   # DOWN
    Vector(-1, 0)   # LEFT
]


def read_input():
    return [
        list(line.rstrip())
        for line in open('input.txt')
    ]


def grid_to_dict(grid):
    return {
        (x, y): grid[y][x]
        for y in range(len(grid))
        for x in range(len(grid[0]))
    }


def part_1(grid):
    pos = Vector(len(grid[0]) // 2, len(grid) // 2)
    direction_idx = 0
    infection_count = 0

    grid_dict = grid_to_dict(grid)

    for _ in range(10_000):
        x, y = pos
        state = grid_dict.get((x, y), '.')

        # Change direction
        if state == '#':
            direction_idx = (direction_idx + 1) % 4
        else:
            direction_idx = (direction_idx - 1) % 4

        # Change state
        if state == '.':
            grid_dict[(x, y)] = '#'
            infection_count += 1
        else:
            grid_dict[(x, y)] = '.'

        pos += DIRECTIONS[direction_idx]

    return infection_count


def part_2(grid):
    pos = Vector(len(grid[0]) // 2, len(grid) // 2)
    direction_idx = 0
    infection_count = 0

    grid_dict = grid_to_dict(grid)

    for i in range(10_000_000):
        show_progress(i / 10000000)
        x, y = pos
        state = grid_dict.get((x, y), '.')

        # Change direction
        if state == '.':
            direction_idx = (direction_idx - 1) % 4
        elif state == '#':
            direction_idx = (direction_idx + 1) % 4
        elif state == 'F':
            direction_idx = (direction_idx + 2) % 4

        # Change state
        if state == '.':
            grid_dict[(x, y)] = 'W'
        elif state == 'W':
            grid_dict[(x, y)] = '#'
            infection_count += 1
        elif state == '#':
            grid_dict[(x, y)] = 'F'
        elif state == 'F':
            grid_dict[(x, y)] = '.'

        pos += DIRECTIONS[direction_idx]
    show_progress(1)

    return infection_count


if __name__ == '__main__':
    grid_input = read_input()

    print(f"Part 1: {part_1(grid_input)}")
    print(f"\nPart 2: {part_2(grid_input)}")
