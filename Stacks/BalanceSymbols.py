# Checks wheather opening symbols and closing symbols viz. "(, {, [, }, ), ]" are balanced.


from StackDynamicArray import Stack
def matches(strng,complstrng):
    if strng == "]":
        strng = "["
    elif strng == ")":
        strng = "("
    elif strng == "}":
        strng = "{"
    return strng == complstrng

def balance_symbols(inp):
    symbol_stack = Stack()
    balanced = False
    for symbols in inp:
        if symbols not in ["(","{","["] and symbol_stack.is_empty():
            balanced = False
        else:
            if symbols in ["(","{","["]:
                symbol_stack.push(symbols)
                balanced = False
            else:
                top_symbol = symbol_stack.pop()
                if matches(symbols, top_symbol):
                    balanced = True
                else:
                    balanced = False
    return balanced
