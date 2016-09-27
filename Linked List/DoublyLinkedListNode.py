class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        self.head = None
        self.tail = None
        self.length = 0

    def set_data(self, data=None):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next=None):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next is not None

    def set_prev(self, prev=None):
        self.prev = prev

    def get_prev(self):
        return self.prev

    def has_prev(self):
        return self.prev is not None

    def list_length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def __str__(self):
        return "Node [Data = %s]" % self.data

    def insert_in_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.set_next(self.head)
            new_node.set_prev(None)
            self.head.set_prev(new_node)
            self.head = new_node
        self.length += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            current_node = self.head
            while current_node.get_next() is not None:
                current_node = current_node.get_next()
            current_node.set_next(new_node)
            new_node.set_prev(current_node)
            self.tail = new_node
        self.length += 1

    def insert_at_position(self, data, position):
        if position < 1 or position > self.length:
            raise ValueError("Invalid Position.")
        elif position == 1:
            self.insert_in_beginning(data)
        elif position == self.length:
            self.insert_at_end(data)
        else:
            new_node = Node(data)
            count = 1
            current_node = self.head
            while count != position:
                current_node = current_node.get_next()
            new_node.set_next(current_node)
            new_node.set_prev(current_node.get_prev())
            current_node.set_prev(new_node)
            current_node.get_prev().set_next(new_node)
            self.length += 1

    def delete_from_beginning(self):
        if self.head is None:
            raise ValueError("Underflow! Linked List is Empty.")
        else:
            current_node = self.head
            self.head = current_node.get_next()
            current_node.set_next(None)
            self.head.set_prev(None)
            self.length -= 1

    def delete_from_end(self):
        if self.head is None:
            raise ValueError("Underflow! Linked List is Empty.")
        else:
            current_node = self.tail
            self.tail = current_node.get_prev()
            current_node.set_prev(None)
            self.tail.set_next(None)
            self.length -= 1

    def delete_at_position(self, position):
        if self.head is None:
            raise ValueError("Underflow! Linked list is Empty.")
        elif position < 1 or position > self.length:
            raise ValueError("Invalid Position.")
        elif position == 1:
            self.delete_from_beginning()
        elif position == self.length:
            self.delete_from_end()
        else:
            count = 1
            current_node = self.head
            previous_node = None
            while count != position:
                previous_node = current_node
                current_node = current_node.get_next()
            previous_node.set_next(current_node.get_next())
            current_node.get_next.set_prev(previous_node)
            current_node.set_prev(None)
            current_node.set_next(None)
            self.length -= 1
