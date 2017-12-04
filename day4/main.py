from collections import Counter


def read_input():
    return [
        line.rstrip().split(' ')
        for line in open('input.txt').readlines()
    ]


def has_no_duplicate(it):
    return max(Counter(it).values()) == 1


def part_1(phrases):
    return len([
        phrase
        for phrase in phrases
        if has_no_duplicate(phrase)
    ])


def part_2(phrases):
    return len([
        phrase
        for phrase in phrases
        if has_no_duplicate([
            tuple(sorted(word))
            for word in phrase
        ])
    ])


if __name__ == "__main__":
    phrases_input = read_input()

    print(f"Part 1: {part_1(phrases_input)}")
    print(f"Part 2: {part_2(phrases_input)}")
