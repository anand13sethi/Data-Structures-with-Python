# Returns tree size using level order intuition.


import Queue


def tree_size(root):
    if root is None:
        return
    queue = Queue.Queue()
    node = root
    count = 0
    queue.put(node)
    while not queue.empty():
        node = queue.get()
        count += 1
        if node.get_left():
            queue.put(node.get_left())
        if node.get_right():
            queue.put(node.get_right())
    return count