def read_input():
    return open('input.txt').read()


def part_1(chars):
    skip = False
    is_garbage = False
    group_depth = 0
    total_score = 0

    for c in chars:
        if skip:
            skip = False
            continue
        if c == '!':
            skip = True
            continue
        if is_garbage:
            if c == '>':
                is_garbage = False
            else:
                continue
        elif c == '<':
            is_garbage = True
        elif c == '{':
            group_depth += 1
        elif c == '}' and group_depth:
            total_score += group_depth
            group_depth -= 1

    return total_score


def part_2(chars):
    skip = False
    is_garbage = False
    garbage_count = 0

    for c in chars:
        if skip:
            skip = False
            continue
        if c == '!':
            skip = True
            continue
        if is_garbage:
            if c == '>':
                is_garbage = False
            else:
                garbage_count += 1
                continue
        elif c == '<':
            is_garbage = True

    return garbage_count


if __name__ == '__main__':
    stream_input = read_input()

    print(f"Part 1: {part_1(stream_input)}")
    print(f"Part 2: {part_2(stream_input)}")
