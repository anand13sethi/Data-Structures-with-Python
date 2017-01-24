# A binary tree node implementation.


class BinaryTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def insert_left(self, data):
        if self.left is None:
            self.left = BinaryTreeNode(data)
        else:
            new_node = BinaryTreeNode(data)
            new_node.left = self.left
            self.left = new_node

    def insert_right(self, data):
        if self.right is None:
            self.right = BinaryTreeNode(data)
        else:
            new_node = BinaryTreeNode(data)
            new_node.right = self.right
            self.right = new_node
