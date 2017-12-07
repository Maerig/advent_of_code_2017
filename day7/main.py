import re
from collections import Counter

from day7.node import Node


NODE_REGEX = re.compile("(.*) \((\d+)\)(?: -> (.*))?")


def read_input():
    return [
        NODE_REGEX.match(line.rstrip()).groups()
        for line in open('input.txt')
    ]


def generate_tree(raw_nodes):
    nodes = {
        name: Node(name, int(weight))
        for name, weight, _ in raw_nodes
    }

    for name, _, children in raw_nodes:
        if children:
            nodes[name].set_children([
                nodes[child.strip()]
                for child in children.split(',')
            ])

    # Return root
    for node in nodes.values():
        if not node.parent:
            return node


def part_1(tree):
    return tree.name


def find_unbalanced(node, expected_weight):
    children_total_weights = [
        (child, child.get_total_weight())
        for child in node.children
    ]
    weight_counts = Counter(
        child_total_weight
        for _, child_total_weight in children_total_weights
    )
    if len(weight_counts) == 1:
        # Children are balanced
        return expected_weight - sum(
            child_total_weight
            for _, child_total_weight in children_total_weights
        )

    balanced_weight, unbalanced_weight = [
        weight
        for weight, _ in weight_counts.most_common(2)
    ]

    unbalanced_node = next(
        child
        for child, child_total_weight in children_total_weights
        if child_total_weight == unbalanced_weight
    )
    return find_unbalanced(unbalanced_node, balanced_weight)


def part_2(tree):
    return find_unbalanced(tree, 0)


if __name__ == '__main__':
    nodes_input = read_input()
    nodes_tree = generate_tree(nodes_input)

    print(f"Part 1: {part_1(nodes_tree)}")
    print(f"Part 2: {part_2(nodes_tree)}")
