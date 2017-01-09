# Queue implementation using dynamic array with repeated doubling and in circular fashion.


class Queue:
    def __init__(self, limit=10):
        self.queue = [None]*limit
        self.rear = limit - 1
        self.front = -1
        self.limit = limit
        self.size = 0

    def is_empty(self):
        return self.size <= 0

    def enqueue(self, data):
        if self.size >= self.limit:
            self.resize()
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

    def resize(self):
        self.limit *= 2
        new_queue = [None]*self.limit
        for i in range(0, len(self.queue)):
            new_queue[i] = self.queue[i]
        self.queue = new_queue

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

    def size(self):
        return self.size
