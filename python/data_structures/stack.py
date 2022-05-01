from data_structures.node import Node

class Stack:

    def __init__(self):
        self.top = None

    def push(self, value):

        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        try:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
        except:
            raise InvalidOperationError("Method not allowed on empty collection")

    def peek(self):
        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            return self.top.value

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

class InvalidOperationError(Exception):
    pass


