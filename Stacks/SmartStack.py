# Stack optimised to get minimum(or maximum) element in O(1) and also memory efficient.


class SmartStack:
    def __init__(self):
        self.stack = []
        self.min_stack =[]

    def peek(self):
        return self.min_stack[len(self.min_stack) - 1]

    def push(self, data):
        if len(self.stack) == 0:
            self.stack.append(data)
            self.min_stack.append(data)
        else:
            self.stack.append(data)
            if data < self.min_stack[len(self.min_stack) - 1]:
                self.min_stack.append(data)

    def pop(self):
        return self.stack.pop()

    def get_min(self):
        return self.min_stack.pop()
