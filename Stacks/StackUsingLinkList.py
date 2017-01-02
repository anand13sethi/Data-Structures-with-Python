# Stack implementation using Link List.
# Growth and Shrinking is more graceful than dynamic array.


class Stack():
    def __init__(self):
        self.data = None
        self.next = None
        self.length = -1

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def list_length(self):
        return self.length

    def print_stack(self):
        if self.length < 0:
            raise ValueError("Empty Stack!")
        current_node = self.head
        while current_node is not None:
            print current_node.get_data()
            current_node = current_node.get_next()

    def push(self, data):
        new_node = Stack()
        new_node.set_data(data)
        if self.length < 0:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
        self.length += 1

    def pop(self):
        if self.length < 0:
            raise ValueError("Underflow!")
        current_node = self.head
        self.head = current_node.get_next()
        current_node.set_next(None)
        print str(current_node.get_data()) + " <- Deleted"
        del current_node
        self.length -= 1

    def peek(self):
        if self.head is None:
            raise ValueError("Peeking In Empty Stack!")
        current_node = self.head
        return current_node.get_data()