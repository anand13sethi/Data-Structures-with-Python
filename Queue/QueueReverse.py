# Reversing a Queue implemented using singly link list using stack.


from QueueUsingLinkList import Queue


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
            raise ValueError("Underflow!")
        else:
            self.size -= 1
            return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise ValueError("Peeking Into Empty Stack!")
        else:
            return self.stack[self.size]


def reverse_queue(que=Queue()):
    aux_stack = Stack()
    if que.is_empty():
        raise ValueError("Empty Queue!")
    else:
        while not que.is_empty():
            aux_stack.push(que.dequeue())
        while not aux_stack.is_empty():
            que.enqueue(aux_stack.pop())
    return que
