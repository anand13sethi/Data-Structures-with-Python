# Stack implementation using static size array.


class Stack:
    def __init__(self, limit=10):
        self.stklist = []
        self.limit = limit
        self.length = -1

    def push(self, data=None):
        if self.length >= self.limit - 1:
            raise ValueError("OverFlow!")
        else:
            self.stklist.append(data)
            self.length += 1

    def pop(self):
        if self.length < 0:
            raise ValueError("UnderFlow!")
        else:
            self.stklist.pop()
            self.length -= 1

    def peek(self):
        if self.length < 0:
            raise ValueError("Peeking Into Empty Stack!")
        else:
            return self.stklist[self.length]

    def stack_length(self):
        return self.length + 1