# A binary tree node implementation.


class BinaryTreeNode:
    def __init__(self):
        self.data = None
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
