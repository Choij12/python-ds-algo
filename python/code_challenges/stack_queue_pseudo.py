from data_structures.stack import Stack

class PseudoQueue:
    def __init__(self) -> None:
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()

    def enqueue(self, value):
        self.enqueue_stack.push(value)

    def dequeue(self):
        while not self.enqueue_stack.is_empty():
            self.dequeue_stack.push(self.enqueue_stack.pop())
        temp = self.dequeue_stack.pop()
        while not self.dequeue_stack.is_empty():
            self.enqueue_stack.push(self.dequeue_stack.pop())

        return temp

    def is_empty(self):
        return self.enqueue_stack.is_empty()
