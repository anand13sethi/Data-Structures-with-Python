# Steps to delete a node in a tree:
# 1. Find the node.
# 2. Find the deepest node.
# 3. Replace data of deepest node with the one to be deleted.
# 4. Delete the deepest node.


import Queue


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def levelorder(root, result):
    if root is None:
        return
    queue = Queue.Queue()
    node = root
    queue.put(node)
    while not queue.empty():
        node = queue.get()
        result.append(node.data)
        if node.left:
            queue.put(node.left)
        if node.right:
            queue.put(node.right)
    return result

def deepest_node(root):
    if root is None:
        return
    queue = Queue.Queue()
    node = root
    queue.put(node)
    while not queue.empty():
        node = queue.get()
        if node.left:
            queue.put(node.left)
        if node.right:
            queue.put(node.right)
    return node.data


def delete_node(root, key):
    if root is None:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        if node.data == key:
            node.data = deepest_node(root)
            return "Deleted "+str(key)
        else:
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return "Key Not Found"



tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)

print delete_node(tree, 3)
print levelorder(tree, list())

# todo: 1. Delete Instance of the deepest node.