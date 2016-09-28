class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        self.length = 0

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next is not None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.set_next(new_node)
        else:
            new_node.set_next(self.head)
            current_node = self.head
            while current_node.get_next() != self.head:
                current_node = current_node.get_next()
            current_node.set_next(new_node)
            self.head = new_node
        self.length += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.set_next(new_node)
        else:
            current_node = self.head
            while current_node.get_next() != self.head:
                current_node = current_node.get_next()
            current_node.set_next(new_node)
            new_node.set_next(self.head)
        self.length += 1
    def insert_at_position(self, data, position):
        if position < 0 or position > self.length:
            raise ValueError("Invalid Position.")
        elif position == 1:
            self.insert_at_beginning()
        elif position == self.length:
            self.insert_at_end()
        else:
            new_node = Node(data)
            count = 1
            current_node = self.head
            previous_node = None
            while count != position:
                previous_node = current_node
                current_node = current_node.get_next()
                count += 1
            new_node.set_next(current_node)
            previous_node.set_next(new_node)
            self.length += 1