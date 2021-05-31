def valid_parenthesis(s):
    stack = []
    parenthesis = {')': '(', '}': '{', ']': '['}
    for c in s:
        if c in ['(', '{', '[']:
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            p = stack.pop()
            if parenthesis[c] != p:
                return False
    return len(stack) == 0


def valid_parenthesis_aster(s):
    # (*) is valid?
    cmin, cmax = 0, 0
    for c in s:
        if c == '(':
            cmin += 1
            cmax += 1
        if c == ')':
            cmin = max(cmin - 1, 0)
            cmax -= 1
        if c == '*':
            cmin = max(cmin - 1, 0)
            cmax += 1
        if cmax < 0:
            return False
    return cmin == 0


if __name__ == '__main__':
    print(valid_parenthesis('[()]{}{[()()]()}'))
    print(valid_parenthesis('[(])'))
    print(valid_parenthesis('}}{{'))
    print(valid_parenthesis(''))

    print(valid_parenthesis_aster('(*)'))
