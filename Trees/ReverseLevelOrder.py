# Returns reversed level order traversal.


import Queue


def reverse_levelorder(root):
    if root is None:
        return
    queue = Queue.Queue()
    stack = list()
    queue.put(root)
    while not queue.empty():
        node = queue.get()
        stack.append(node.get_data())
        if node.get_right() is not None:
            queue.put(node.get_right)()
        if node.get_left() is not None:
            queue.put(node.get_left())
    return stack