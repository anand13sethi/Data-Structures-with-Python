# Removes duplicate pairs using stack.
# eg: careermonk -> camonk


from StackDynamic import Stack


def remove_duplicate_pairs(stack):
    new_stack = Stack()
    while not stack.is_empty():
        new_stack.push(stack.pop())
        if not stack.is_empty() and new_stack.peek() == stack.peek():
            while not stack.is_empty() and new_stack.peek() == stack.peek():
                new_stack.pop()
                stack.pop()
    return new_stack
