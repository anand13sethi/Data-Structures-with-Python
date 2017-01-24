# Search an element in tree (recursive and iterative).


import Queue


def search_recursive(root, item):
    if root is None:
        return False
    node = root
    if node.get_data() == item:
        return True
    search_recursive(node.get_left(), item)
    search_recursive(node.get_right(), item)


def search_iterative(root, item):
    if root is None:
        return False
    queue = Queue.Queue()
    queue.put(root)
    while not queue.empty():
        node = queue.get()
        if node.get_data() == item:
            return True
        if node.get_left() is not None:
            queue.put(node.get_left())
        if node.get_right() is not None:
            queue.put(node.get_right())
