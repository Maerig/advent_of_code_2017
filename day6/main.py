def read_input():
    return [
        int(block)
        for block in open('input.txt').read().rstrip().split('\t')
    ]


def distribute(blocks, src_idx):
    remaining = blocks[src_idx]
    blocks[src_idx] = 0
    i = (src_idx + 1) % len(blocks)
    while remaining > 0:
        blocks[i] += 1
        remaining -= 1
        i = (i + 1) % len(blocks)


def run_until_loop(blocks):
    visited_states = set()
    visited_states.add(tuple(blocks))

    while True:
        max_index = blocks.index(max(blocks))
        distribute(blocks, max_index)
        state = tuple(blocks)
        if state in visited_states:
            return blocks, len(visited_states)
        visited_states.add(state)


def part_1(blocks):
    return run_until_loop(blocks)[1]


def part_2(blocks):
    loop_first_state = run_until_loop(blocks)[0]
    return run_until_loop(loop_first_state)[1]


if __name__ == '__main__':
    blocks_input = read_input()

    print(f"Part 1: {part_1(blocks_input)}")
    print(f"Part 2: {part_2(blocks_input)}")
