class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class LazyNode:
    def __init__(self, value):
        self.value = value
        self._node = None

    @property
    def node(self):
        if self._node is None:
            self._node = Node(self.value)
        return self._node

def bin_bes_derevo(root_value):
    while True:
        action = input("node для получения узла, quit для выхода: ")
        if action == "node":
            for _ in range(5):
                yield LazyNode(root_value).node
        elif action == "quit":
            break

tree_generator = bin_bes_derevo(1)
for node in tree_generator:
    print(node.value)
