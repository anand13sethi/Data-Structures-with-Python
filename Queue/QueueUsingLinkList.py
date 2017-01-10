# Queue implementation using link list.


class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size <= 0

    def enqueue(self, data):
        new_node = Node()
        new_node.set_data(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.set_next(new_node)
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Underflow!")
        else:
            current_node = self.front
            self.front = current_node.get_next()
            item = current_node.get_data()
            del current_node
            self.size -= 1
            return item

    def queue_rear(self):
        if self.is_empty():
            raise ValueError("Empty Queue!")
        else:
            item = self.rear.get_data()
            return item

    def queue_front(self):
        if self.is_empty():
            raise ValueError("Empty Queue!")
        else:
            item = self.front.get_data()
            return item

    def size(self):
        return self.size
