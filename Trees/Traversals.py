# Tree traversals viz. PreOrder, InOrder, PostOrder and LevelOrder (recursive and iterative).


def preorder_recursive(root, result=[]):
    if root is None:
        return
    result.append(root.data())
    preorder_recursive(root.left())
    preorder_recursive(root.right())


def preorder_iterative(root, result=[]):
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

# TODO - 1. Add InOrder Traversal
# TODO - 2. Add PostOrder Traversal
# TODO - 2. Add LevelOrder Traversal
