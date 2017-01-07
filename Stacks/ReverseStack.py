# Code to reverse elements of a stack by using only stack operations push() nad pop().


from StackDynamic import Stack


def reverse_stack(stk):
    new_stack = Stack()
    while not stk.is_empty():
        new_stack.push(stk.pop())
    return new_stack
