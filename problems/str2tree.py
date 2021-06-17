class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        val = val
        left = left
        right = right


def str2tree(s):
    if len(s) == 0:
        return None
    pos_pairs = get_pos_pairs(s)
    val, pos = parse_val(s, 0)
    root = TreeNode(val)
    root.left = _str2tree(
        s, pos_pairs, pos + 1, pos_pairs.get(pos, -1) - 1)
    next_pos = pos_pairs.get(pos, -1) + 1
    root.right = _str2tree(
        s, pos_pairs, next_pos + 1, pos_pairs.get(next_pos, -1) - 1)
    return root


def _str2tree(s, pos_pairs, left, right):
    if left > right:
        return None
    val, pos = parse_val(s, left)
    root = TreeNode(val)
    root.left = _str2tree(
        s, pos_pairs, pos + 1, pos_pairs.get(pos, -1) - 1)
    next_pos = pos_pairs.get(pos, -1) + 1
    root.right = _str2tree(
        s, pos_pairs, next_pos + 1, pos_pairs.get(next_pos, -1) - 1)
    return root


def parse_val(s, pos):
    valstr = []
    while pos < len(s) and s[pos] != '(' and s[pos] != ')':
        valstr.append(s[pos])
        pos += 1
    return int(''.join(valstr)), pos


def get_pos_pairs(s):
    pos_pairs = {}
    stack = []
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            pos = stack.pop()
            pos_pairs[pos] = i
    return pos_pairs
