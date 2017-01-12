# Stack implementation using 2 Queues.
# Queue implemented is by using dynamic arrays with repeated doubling.


class Queue:
    def __init__(self, limit=10):
        self.queue = [None]*limit
        self.front = -1
        self.rear = limit-1
        self.limit = limit
        self.size = 0

    def is_last(self):
        if (self.front+1) % self.limit == self.rear or (self.front-1) % self.limit == self.rear:
            return True

    def is_empty(self):
        return self.size <= 0

    def enqueue(self, data):
        if self.size >= self.limit:
            self.resize()
        self.rear = (self.rear+1) % self.limit
        self.queue[self.rear] = data
        self.size += 1

    def dequeue(self):
        self.front = (self.front+1) % self.limit
        self.size -= 1
        return self.queue[self.front]

    def resize(self):
        self.limit *= 2
        new_queue = [None]*self.limit
        for i in range(0, self.size+1):
            new_queue[i] = self.queue[i]
        self.queue = new_queue
        del new_queue

    def size(self):
        return self.size

    def queue_rear(self):
        return self.queue[self.rear]


class Stack:
    def __init__(self, limit=10):
        self.que1 = Queue(limit)
        self.que2 = Queue(limit)
        self.size = 0

    def is_empty(self):
        return self.size <= 0

    def push(self, data):
        if self.que1.is_empty() and self.que2.is_empty():
            self.que2.enqueue(data)
        else:
            self.que1.enqueue(data)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Underflow!")
        elif self.que1.size > self.que2.size:
            while not self.que1.is_last():
                self.que2.enqueue(self.que1.dequeue())
            self.size -= 1
            return self.que1.dequeue()
        else:
            while not self.que2.is_last():
                self.que1.enqueue(self.que2.dequeue())
            self.size -= 1
            return self.que2.dequeue()
