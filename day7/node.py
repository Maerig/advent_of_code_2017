class Node(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

        self.children = []
        self.parent = None

    def set_children(self, nodes):
        self.children = nodes
        for node in nodes:
            node.parent = self

    def get_total_weight(self):
        return self.weight + sum(
            child.get_total_weight()
            for child in self.children
        )
