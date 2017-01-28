# Returns maximum depth of a given tree using level order traversal intuition.


def max_depth(root):
    if root is None:
        return 0
    else:
        level = 0
        this_level = [root]
        while this_level:
            next_level = list()
            for node in this_level:
                if node.right:
                    next_level.append(node.right)
                if node.left:
                    next_level.append(node.left)
            this_level = next_level
            level += 1
    return level
