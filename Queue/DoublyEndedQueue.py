# Implementation of Doubly Ended Queue.
# Both insertions and deletions can take place from front as well as rear.


class Deque:
    def __init__(self):
        self.queue = []
        self.size = 0

    def is_empty(self):
        return self.size <= 0

    def enqueue_rear(self, data):
        self.queue.append(data)
        self.size += 1

    def enqueue_front(self, data):
        self.queue.insert(0, data)
        self.size += 1

    def dequeue_rear(self):
        self.size -= 1
        return self.queue.pop()

    def dequeue_front(self):
        self.size -= 1
        return self.queue.pop(0)

    def size(self):
        return self.size
