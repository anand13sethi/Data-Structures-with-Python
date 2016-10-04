class Node:
    def __init__(self):
        self.data = None
        self.next = None
        self.length = 0

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next is not None

    def list_length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def print_linked_list(self):
        if self.head is None:
            print "Linked List does not Exist."
        else:
            current_node = self.head
            while current_node is not None:
                print current_node.get_data()
                current_node = current_node.get_next()

    def insert_at_beginning(self, data):
        new_node = Node()
        new_node.set_data(data)
        if self.length == 0:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
        self.length += 1

    def insert_at_end(self, data):
        new_node = Node()
        new_node.set_data(data)
        current = self.head
        while current.get_next() is not None:
            current = current.get_next()

        current.set_next(new_node)
        self.length += 1

    def insert_at_middle(self, position, data):
        if position > self.length+1 or position < 0:
            return None
        elif position == 0:
            self.insert_at_beginning(data)
        elif position == self.length+1:
            self.insert_at_end(data)
        else:
            new_node = Node()
            new_node.set_data(data)
            count = 1
            current_node = self.head
            previous_node = None
            while count != position:
                count += 1
                previous_node = current_node
                current_node = current_node.get_next()
            new_node.set_next(current_node)
            previous_node.set_next(new_node)
            self.length += 1

    def delete_from_beginning(self):
        if self.length == 0:
            raise ValueError("Underflow! Linked List is Empty.")
        else:
            self.head = self.head.get_next()
            self.length -= 1

    def delete_from_end(self):
        if self.length == 0:
            raise ValueError("Underflow! Linked List is Empty.")
        else:
            current_node = self.head
            previous_node = self.head
            while current_node.get_next() is not None:
                previous_node = current_node
                current_node = current_node.get_next()
            previous_node.set_next(None)
            self.length -= 1

    def delete_from_middle_with_node(self, node):
        if self.length == 0:
            raise ValueError("Underflow! Linked List is Empty.")
        else:
            current_node = self.head
            previous_node = None
            found_flag = False
            while not found_flag:
                if current_node == node:
                    found_flag = True
                elif current_node is None:
                    raise ValueError("Node not Present in Linked List.")
                else:
                    previous_node = current_node
                    current_node = current_node.get_next()
        if previous_node is None:
            self.head = current_node.get_next()
        else:
            previous_node.set_next(current_node.get_next())
        self.length -= 1

    def delete_from_middle_with_value(self, value):
        if self.length == 0:
            raise ValueError("Underflow! Linked List is Empty.")
        else:
            current_node = self.head
            previous_node = None
            found_flag = False
            while not found_flag:
                if current_node.get_data() == value:
                    found_flag = True
                elif current_node is None:
                    raise ValueError("No Node With Input Data.")
                else:
                    previous_node = current_node
                    current_node = current_node.get_next()
            if previous_node is None:
                self.head = current_node.get_next()
            else:
                previous_node.set_next(current_node.get_next())
            self.length -= 1

    def delete_at_position(self, position):
        if self.length == 0:
            raise ValueError("Underflow! Linked List Empty.")
        elif position > self.length+1 or position < 0:
            raise ValueError("Invalid Position.")
        else:
            count = 1
            current_node = self.head
            previous_node = None
            while count != position:
                previous_node = current_node
                current_node = current_node.get_next()
                count += 1
            if previous_node is None:
                self.head = current_node.get_next()
            else:
                previous_node.set_next(current_node.get_next())
            self.length -= 1

    def nth_node_from_end(self, n):
        if n < 0:
            if n > self.length:
                raise ValueError("Invalid Position.")
        else:
            ptr_nth = self.head
            ptr_temp = self.head
            moves = 0
            while ptr_temp.get_next() is not None:
                ptr_temp = ptr_temp.get_next()
                moves += 1
                if moves == n:
                    ptr_nth = ptr_nth.get_next()
                elif moves > n:
                    ptr_nth = ptr_nth.get_next()
            print ptr_nth.get_data()
