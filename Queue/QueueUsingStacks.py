# Efficient approach to implement Queue using 2 Stacks.
# Stacks reverses the order of the elements pushed into it but Queue doesn't.
# So basic idea is to do double reversal of elements through Stacks.


class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def is_empty(self):
        return self.size <= 0

    def push(self, data):
        self.stack.append(data)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Underflow!")
        self.size -= 1
        return self.stack.pop()

    def peek(self):
        return self.stack[self.size]


class Queue:
    def __init__(self):
        self.front_stack = Stack()
        self.rear_stack = Stack()
        self.size = 0

    def is_empty(self):
        return self.size <= 0

    def enqueue(self, data):
        self.rear_stack.push(data)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Underflow!")
        elif self.front_stack.is_empty():
            while not self.rear_stack.is_empty():
                self.front_stack.push(self.rear_stack.pop())
        self.size -= 1
        return self.front_stack.pop()
