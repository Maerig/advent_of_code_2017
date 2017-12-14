from day10.main import part_2 as knot_hash


INPUT = 'ffayrhll'
SIZE = 128


def generate_grid(seed):
    return [
        bin(int(knot_hash(f"{seed}-{i}"), 16))[2:].zfill(SIZE)
        for i in range(SIZE)
    ]


def part_1(grid):
    return sum(
        int(d)
        for row in grid
        for d in row
    )


def get_neighbours(x, y):
    return [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1)
    ]


def extract_neighbours(square, squares):
    neighbours = []

    for neighbour in get_neighbours(*square):
        if neighbour in squares:
            neighbours.append(neighbour)
            squares.remove(neighbour)

    return neighbours, squares


def extract_region(source_square, remaining_squares):
    region = []
    new_squares = [source_square]

    while new_squares:
        source_square = new_squares.pop()
        neighbours, remaining_squares = extract_neighbours(source_square, remaining_squares)
        new_squares += neighbours
        region.append(source_square)

    return region, remaining_squares


def part_2(grid):
    remaining_squares = {
        (x, y)
        for y in range(SIZE)
        for x in range(SIZE)
        if grid[y][x] == '1'
    }
    regions = []

    while remaining_squares:
        source_square = remaining_squares.pop()
        region, remaining_squares = extract_region(source_square, remaining_squares)
        regions.append(region)

    return len(regions)


if __name__ == '__main__':
    grid_input = generate_grid(INPUT)

    print(f"Part 1: {part_1(grid_input)}")
    print(f"Part 2: {part_2(grid_input)}")
