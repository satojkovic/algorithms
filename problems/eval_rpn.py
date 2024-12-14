def eval_rpn(tokens):
    ops = ['+', '-', '*', '/']
    stack = []
    for token in tokens:
        if token in ops:
            b = stack.pop()
            a = stack.pop()
            stack.append(calc(a, b, token))
        else:
            stack.append(int(token))
    return stack[0]

def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return int(a / b)


def test_eval_rpn():
    assert eval_rpn(["2","1","+","3","*"]) == 9
    assert eval_rpn(["4","13","5","/","+"]) == 6
    assert eval_rpn(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22

