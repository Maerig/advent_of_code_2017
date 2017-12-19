from day19.vector import Vector


def read_input():
    return [
        line.rstrip()
        for line in open('input.txt')
    ]


def get_segment(diagram, x, y):
    try:
        segment = diagram[y][x]
    except IndexError:
        return None

    if not segment.strip():
        # Empty
        return None

    return segment


def get_neighbours(diagram, x, y):
    return [
        Vector(i, j)
        for i, j in [
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1)
        ]
        if get_segment(diagram, i, j)
    ]


def get_next_pos(diagram, current, prev):
    segment = get_segment(diagram, *current)
    if segment == '|' or segment == '-':
        # Continue in the same direction
        return current + current - prev

    # Else continue to neighbour which isn't prev
    for neighbour in get_neighbours(diagram, *current):
        if neighbour != prev:
            return neighbour

    # Nowhere to go
    return None


def navigate(diagram):
    x = diagram[0].index('|')
    current = Vector(x, 0)
    prev = Vector(x, -1)

    while current:
        yield current
        prev, current = current, get_next_pos(diagram, current, prev)


def part_1(diagram):
    letters = []

    for position in navigate(diagram):
        content = get_segment(diagram, *position)
        if content not in ('|', '-', '+'):
            letters.append(content)

    return ''.join(letters)


def part_2(diagram):
    return len(list(navigate(diagram)))


if __name__ == '__main__':
    diagram_input = read_input()

    print(f"Part 1: {part_1(diagram_input)}")
    print(f"Part 2: {part_2(diagram_input)}")


