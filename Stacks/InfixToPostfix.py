# Outputs a postfix expression of the given infix expression.


from StackDynamicArray import Stack

prec = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3, '**': 4}


def infix_to_postfix(infixexpr):
    tokenlist = infixexpr.split()
    op_stack = Stack()
    postfix_list = []
    for token in tokenlist:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789' or token in 'abcdefghijklmnopqrstuvwxyz':
            postfix_list.append(token)
        elif token is '(':
            op_stack.push(token)
        elif token in ['+', '-', '*', '/', '**']:
            if op_stack.is_empty():
                op_stack.push(token)
            elif prec[op_stack.peek()] >= prec[token]:
                while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                    postfix_list.append(op_stack.pop())
                op_stack.push(token)
            else:
                op_stack.push(token)
        elif token is ')':
            top_token = op_stack.pop()
            while top_token is not '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)
