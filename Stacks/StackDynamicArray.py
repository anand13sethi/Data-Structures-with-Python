# Stack implementation using array with repeated doubling.
# Optimal approach than iterative.


class Stack:
    def __init__(self, limit=10):
        self.stklist = []
        self.limit = limit
        self.length = -1

    def push(self, data):
        if self.length >= self.limit - 1:
            self.resize()
        self.stklist.append(data)
        self.length += 1

    def pop(self):
        if self.length < 0:
            raise ValueError("Underflow!")
        else:
            self.stklist.pop()
            self.length -= 1

    def peek(self):
        if self.length < 0:
            raise ValueError("Peeking Into Empty Stack!")
        else:
            return self.stklist[self.length]

    def resize(self):
        new_stklist = list(self.stklist)
        self.limit *= 2
        self.stklist = new_stklist

    def stack_length(self):
        print "Total Length: " + str(self.limit)
        print "Elements In Stack: " + str(self.length + 1)