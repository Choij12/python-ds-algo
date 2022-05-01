from data_structures.node import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        if self.rear:
            self.rear.next = Node(value)
            self.rear = self.rear.next
        else:
            self.rear = Node(value)
            self.front = self.rear

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

