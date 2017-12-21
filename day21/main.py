INITIAL_GRID = [
    ['.', '#', '.'],
    ['.', '.', '#'],
    ['#', '#', '#']
]


def read_input():
    rules = {}

    for line in open('input.txt'):
        left, right = line.split('=>')
        rules[left.strip()] = right.strip()

    return rules


def square_to_slashes(square):
    return '/'.join(
        ''.join(row) for row in square
    )


def slashes_to_square(slashes):
    return [
        list(row)
        for row in slashes.split('/')
    ]


def flip_v(square):
    return [
        square[j]
        for j in reversed(range(len(square)))
    ]


def flip_h(square):
    return [
        [
            row[i]
            for i in reversed(range(len(square)))
        ]
        for row in square
    ]


def rotate(square):
    size = len(square)
    return [
        [
            square[i][j]
            for i in reversed(range(size))
        ]
        for j in range(size)
    ]


def get_variations(square):
    for _ in range(4):
        yield square
        yield flip_v(square)
        yield flip_h(square)
        square = rotate(square)


def apply_rules(square, rules):
    for variation in get_variations(square):
        slashes = square_to_slashes(variation)
        if slashes in rules:
            return slashes_to_square(rules[slashes])
    raise ValueError(square)


def split_grid(grid):
    grid_size = len(grid)
    square_size = 2 if (grid_size % 2 == 0) else 3

    return [  # Square rows
        [  # Squares
            [
                sub_row[square_idx * square_size: square_idx * square_size + square_size]
                for sub_row in grid[square_row_idx * square_size: square_row_idx * square_size + square_size]
            ]
            for square_idx in range(grid_size // square_size)
        ]
        for square_row_idx in range(grid_size // square_size)
    ]


def join_squares(squares):
    square_size = len(squares[0][0])
    grid_size = len(squares[0]) * square_size

    return [
        [
            squares[j // square_size][i // square_size][j % square_size][i % square_size]
            for i in range(grid_size)
        ]
        for j in range(grid_size)
    ]


def enhance(grid, rules, iterations):
    for _ in range(iterations):
        squares = split_grid(grid)
        new_squares = [
            [
                apply_rules(square, rules)
                for square in square_row
            ]
            for square_row in squares
        ]
        grid = join_squares(new_squares)

    return grid


def count_symbol(grid, symbol):
    return sum(
        1
        for row in grid
        for elt in row
        if elt == symbol
    )


def part_1(rules):
    grid = enhance(INITIAL_GRID, rules, 5)
    return count_symbol(grid, '#')


def part_2(rules):
    grid = enhance(INITIAL_GRID, rules, 18)
    return count_symbol(grid, '#')


if __name__ == '__main__':
    rules_input = read_input()

    print(f"Part 1: {part_1(rules_input)}")
    print(f"Part 2: {part_2(rules_input)}")
