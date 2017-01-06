# Stack implementation using builtin data structure List.
# List is in itself uses LIFO order.


class Stack:
    def __init__(self):
        self.stklist = []
        self.length = -1

    def push(self, data=None):
        self.stklist.append(data)
        self.length += 1

    def pop(self):
        if self.length < 0:
            raise ValueError("UnderFlow!")
        else:
            self.length -= 1
            return self.stklist.pop()

    def peek(self):
        if self.length < 0:
            raise ValueError("Peeking Into Empty Stack!")
        else:
            return self.stklist[self.length]

    def stack_length(self):
        return self.length + 1

    def is_empty(self):
        return len(self.stklist) == 0
