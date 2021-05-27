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


if __name__ == '__main__':
    print(valid_parenthesis('[()]{}{[()()]()}'))
    print(valid_parenthesis('[(])'))
    print(valid_parenthesis('}}{{'))
    print(valid_parenthesis(''))
