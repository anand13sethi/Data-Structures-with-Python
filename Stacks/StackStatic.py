class Stack:
    def __init__(self, length=10):
        self.stklist = []
        self.max_length = length
        self.length = 0

    def push(self, data=None):
        if self.length >= self.max_length:
            raise ValueError("OverFlow!")
        else:
            self.stklist.append(data)
            self.length += 1

    def pop(self):
        if self.length <= 0:
            raise ValueError("UnderFlow!")
        else:
            self.stklist.pop()
            self.length -= 1

    def peek(self):
        if self.length <= 0:
            raise ValueError("Peeking Into Empty Stack!")
        else:
            return self.stklist[self.length - 1]

    def stack_length(self):
        return self.length