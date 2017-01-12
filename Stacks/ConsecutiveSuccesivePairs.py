# Returns True if the pairs in the given stack are consecutive either increasing or decreasing.
# If stack size is odd we neglect the top element.


from StackDynamic import Stack


def check_consecutive_pairs(stack=Stack()):
    rev_stack = Stack()
    while not stack.is_empty():
        rev_stack.push(stack.pop())
    if rev_stack.stack_length() % 2 == 0:
        while not rev_stack.is_empty():
            a = rev_stack.pop()
            b = rev_stack.pop()
            if abs(a - b) != 1:
                return False
    else:
        for i in range(0, rev_stack.stack_length()/2):
            a = rev_stack.pop()
            b = rev_stack.pop()
            if abs(a - b) != 1:
                return False
    return True
