# Outputs the number of leaves in a binary tree.


def number_of_leaves(root):
    if root is None:
        return
    count = 0
    node = root
    stack = list()
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if not node.left and not node.right:
                count += 1
            node = node.right
    return count
