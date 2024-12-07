def valid_parenthesis(s):
    paren = {")": "(", "}": "{", "]": "["}
    stack = []
    for c in s:
        if c in paren:
            if stack and stack[-1] == paren[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False


def test_valid_parenthesis():
    assert valid_parenthesis("()")
    assert valid_parenthesis("(){}[]")
    assert not valid_parenthesis("(]")
    assert not valid_parenthesis("([)]")
    assert valid_parenthesis("{()}")
    assert not valid_parenthesis("(((")
    assert not valid_parenthesis(")))))")


def valid_parenthesis_aster(s):
    # (*) is valid?
    cmin, cmax = 0, 0
    for c in s:
        if c == "(":
            cmin += 1
            cmax += 1
        if c == ")":
            cmin = max(cmin - 1, 0)
            cmax -= 1
        if c == "*":
            cmin = max(cmin - 1, 0)
            cmax += 1
        if cmax < 0:
            return False
    return cmin == 0


def test_valid_parenthesis_aster():
    assert valid_parenthesis_aster("(*)") is True
