# Evaluates postfix expression using stack.


from StackDynamicArray import Stack


def do_math(opt, op1, op2):
    if opt == '*':
        return op1 * op2
    elif opt == '+':
        return op1 + op2
    elif opt == '-':
        return op1 - op2
    elif opt == '/':
        return op1 / op2
    elif opt == '**':
        return op1 ** op2


def evaluate_expression(postfix):
    eval_stack = Stack()
    for token in postfix:
        if token in ['+', '-', '*', '/', '**']:
            opt = token
            op2 = float(eval_stack.pop())
            op1 = float(eval_stack.pop())
            eval_stack.push(do_math(opt, op1, op2))
        else:
            eval_stack.push(token)
    return eval_stack.pop()

print evaluate_expression('123*+5-')