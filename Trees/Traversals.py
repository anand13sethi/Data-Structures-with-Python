# Tree traversals viz. PreOrder, InOrder, PostOrder and LevelOrder (recursive and iterative).


import Queue


def preorder_recursive(root, result):
    if root is None:
        return
    result.append(root.get_data())
    preorder_recursive(root.get_left(), result)
    preorder_recursive(root.get_right(), result)
    return result


def preorder_iterative(root, result):
    if root is None:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.get_data())
        if node.get_right():
            stack.append(node.get_right())
        if node.get_left():
            stack.append(node.get_left())
    return result


def inorder_recursive(root, result):
    if root is None:
        return
    inorder_recursive(root.get_left(), result)
    result.append(root.get_data())
    inorder_recursive(root.get_right(), result)
    return result


def inorder_iterative(root, result):
    if root is None:
        return
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.get_left()
        else:
            node = stack.pop()
            result.append(node.get_data())
            node = node.get_right()
    return result


def postorder_recursive(root, result):
    if root is None:
        return
    postorder_recursive(root.get_left(), result)
    postorder_recursive(root.get_right(), result)
    result.append(root.get_data())
    return result


def postorder_iterative(root, result):
    if root is None:
        return
    stack = []
    visited = set()
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.get_left()
        else:
            node = stack.pop()
            if node.get_right() and node.get_right() not in visited:
                stack.append(node)
                node = node.get_right()
            else:
                result.append(node.get_data())
                visited.add(node)
                node = None
    return result


def levelorder(root, result):
    if root is None:
        return
    queue = Queue.Queue()
    node = root
    queue.put(node)
    while not queue.empty():
        node = queue.get()
        result.append(node.get_data())
        if node.left:
            queue.put(node.get_left())
        if node.right:
            queue.put(node.get_right())
    return result
