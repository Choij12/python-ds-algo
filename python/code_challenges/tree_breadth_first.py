class Node:

    def __init__(self, data=None, next=None):
        self.value = data
        self.next = next

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):

        if not self.front:
            self.front = Node(value)
            self.rear = self.front
        else:
            self.rear.next = Node(value)
            self.rear = self.rear.next

    def dequeue(self):

        if self.front is None:
            raise InvalidOperationError
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value

    def peek(self):
        if not self.front:
            raise InvalidOperationError
        else:
            return self.front.value

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

class InvalidOperationError(Exception):
    pass

def breadth_first(tree):
    breadth = Queue()
    tree_values = []

    if not tree:
        return tree_values
    if not tree.root:
        return tree_values
    if not breadth.front:
        breadth.enqueue(tree.root)
    while breadth.front:
        root = breadth.dequeue()
        tree_values.append(root.value)
        if root.left:
            breadth.enqueue(root.left)
        if root.right:
            breadth.enqueue(root.right)


    return(tree_values)
