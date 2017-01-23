# Finding maximum element in a tree (recursive and iterative).


import Queue


def get_max_recursive(root):
    max_elem = float("-infinity")
    if root is None:
        return max_elem
    else:
        if root.get_data() > max_elem:
            max_elem = root.get_data()
        get_max_recursive(root.get_left())
        get_max_recursive(root.get_right())
        return max_elem


def get_max_iterative(root):
    max_elem = float("-infinity")
    if root is None:
        return max_elem
    else:
        queue = Queue.Queue()
        queue.put(root)
        max_elem = root.get_data()
        while not queue.empty():
            node = queue.get()
            if max_elem < node.get_data():
                max_elem = node.get_data()
            if node.get_left():
                queue.put(node.get_left())
            if node.get_right():
                queue.put(node.get_right())
    return max_elem
