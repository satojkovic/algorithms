def valid_parenthesis(s):
    stack = []
    parenthesis = {")": "(", "}": "{", "]": "["}
    for c in s:
        if c in {")", "}", "]"}:
            if len(stack) == 0 or parenthesis[c] != stack[-1]:
                return False
        else:
            stack.append(c)
    return len(stack) == 0


def test_valid_parenthesis():
    assert valid_parenthesis("()") is True
    assert valid_parenthesis("(){}[]") is True
    assert valid_parenthesis("(]") is False
    assert valid_parenthesis("([)]") is False
    assert valid_parenthesis("{()}") is True


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
