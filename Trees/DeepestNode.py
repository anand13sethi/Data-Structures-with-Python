# Return the deepest node(s) in the tree.


def deepest_level(root):
    if root is None:
        return
    this_level = [root]
    deepest_node = list()
    next_level = list()
    while this_level:
        deepest_node = map(lambda i: i.data, this_level)
        for node in this_level:
            next_level = list()
            if node.right:
                next_level.append(node.right)
            if node.left:
                next_level.append(node.left)
        this_level = next_level
    return deepest_node


