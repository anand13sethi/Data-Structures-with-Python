# Tree traversals viz. PreOrder, InOrder, PostOrder and LevelOrder (recursive and iterative).


import Queue


def preorder_recursive(root, result):
    if root is None:
        return
    result.append(root.data())
    preorder_recursive(root.left, result)
    preorder_recursive(root.right, result)


def preorder_iterative(root, result):
    if root is None:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def inorder_recursive(root, result):
    if root is None:
        return
    inorder_recursive(root.left, result)
    result.append(root.data)
    inorder_recursive(root.right, result)


def inorder_iterative(root, result):
    if root is None:
        return
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            result.append(node.data)
            node = node.right


def postorder_recursive(root, result):
    if root is None:
        return
    postorder_recursive(root.left, result)
    postorder_recursive(root.right, result)
    result.append(root.data)


def postorder_iterative(root, result):
    if root is None:
        return
    stack = []
    visited = set()
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.right and node.right not in visited:
                stack.append(node)
                node = node.right
            else:
                result.append(node.data)
                visited.add(node)
                node = None


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
