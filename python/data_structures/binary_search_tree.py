from data_structures.binary_tree import BinaryTree
from data_structures.binary_tree import Node

class BinarySearchTree(BinaryTree):

    def __init__(self):
        super().__init__()

    def add(self, value):
        node = Node(value)

        def walk(root, new_node):
            if not root:
                return
            new_value = new_node.value
            if new_value < root.value:
                if root.left:
                    walk(root.left, new_node)
                else:
                    root.left = new_node
            else:
                if root.right:
                    walk(root.right, new_node)
                else:
                    root.right = new_node
        if not self.root:
            self.root = node
            return
        walk(self.root, node)

    def contains(self, value):
        def walk(root, value):
            if not root:
                return False
            return (root.value == value or walk(root.left, value) or walk(root.right, value))
        return walk(self.root, value)
