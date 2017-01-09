# Queue implementation using a static array in circular fashion.


class Queue:
    def __init__(self, limit=10):
        self.queue = [None] * limit
        self.front = 0
        self.rear = limit - 1
        self.limit = limit
        self.size = 0

    def is_empty(self):
        return self.size <= 0

    def enqueue(self, data):
        if self.size >= self.limit:
            raise ValueError("Overflow!")
        else:
            self.rear = (self.rear+1) % self.limit
            self.queue[self.rear] = data
            self.size += 1

    def dequeue(self):
        if self.size <= 0:
            raise ValueError("Underflow!")
        else:
            self.front = (self.front+1) % self.limit
            self.size -= 1
            return self.queue[self.front]

    def queue_rear(self):
        if self.is_empty():
            raise ValueError("Empty Queue!")
        else:
            return self.queue[self.rear]

    def queue_front(self):
        if self.is_empty():
            raise ValueError("Empty Queue!")
        else:
            return self.queue[self.front]
