# Circular Link List implementation.


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        self.length = 0
        self.head = None

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next is not None

    def list_length(self):
        if self.head is None:
            print '0'
        else:
            count = 1
            next_node = self.head.get_next()
            while next_node != self.head:
                count += 1
                next_node = next_node.get_next()
            return count

    def print_linked_list(self):
        if self.head is None:
            print 'Linked List does not Exist.'
        else:
            current_node = self.head
            print current_node.get_data()
            current_node = current_node.get_next()
            while current_node != self.head:
                print current_node.get_data()
                current_node = current_node.get_next()

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
        if position < 0 or position > self.length+1:
            raise ValueError("Invalid Position.")
        elif position == 0:
            self.insert_at_beginning(data)
        elif position == self.length+1:
            self.insert_at_end(data)
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

    def delete_from_beginning(self):
        if self.head is None:
            raise ValueError("Underflow! Linked List is Empty.")
        else:
            current_node = self.head
            next_node = current_node.get_next()
            while next_node.get_next() != self.head:
                next_node = next_node.get_next()
            next_node.set_next(current_node.get_next())
            self.head = current_node.get_next()
            current_node.set_next(None)
            self.length -= 1

    def delete_from_end(self):
        if self.head is None:
            raise ValueError("Underflow! Linked List is Empty.")
        else:
            current_node = self.head
            previous_node = None
            while current_node.get_next() != self.head:
                previous_node = current_node
                current_node = current_node.get_next()
            previous_node.set_next(self.head)
            current_node.set_next(None)
            self.length -= 1

    def delete_from_position(self, position):
        if self.head is None:
            raise ValueError("Underflow! Linked List is Empty.")
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
                count += 1
            previous_node.set_next(current_node.get_next())
            current_node.set_next(None)
            self.length -= 1