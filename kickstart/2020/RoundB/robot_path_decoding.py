def push(col_moves, row_moves, c):
    if c == '(':
        col_moves.append(c)
        row_moves.append(c)
    elif c == 'E' or c == 'W':
        move = 1 if c == 'E' else -1
        col_moves.append(move)
    elif c == 'N' or c == 'S':
        move = -1 if c == 'N' else 1
        row_moves.append(move)
    return col_moves, row_moves


def update(moves, X):
    i = len(moves) - 1
    move = 0
    while i >= 0 and moves[i] != '(':
        move += moves.pop()
        i -= 1
    moves.pop()
    moves.append(move * X)
    return moves


def parentheses(program):
    p = {}
    stack = []
    for i, c in enumerate(program):
        if c == '(':
            stack.append(i)
        elif c == ')':
            j = stack.pop()
            p[j] = i
    return p


def robot_path_decoding():
    T = int(input())
    for t in range(1, T + 1):
        program = input()
        col_moves = []
        row_moves = []
        Xs = []
        for c in program:
            if c == ')':
                X = Xs.pop()
                col_moves = update(col_moves, X)
                row_moves = update(row_moves, X)
            elif c in ['(', 'N', 'S', 'E', 'W']:
                col_moves, row_moves = push(col_moves, row_moves, c)
            elif c in '23456789':
                Xs.append(int(c))
        col_end = 1 + sum(col_moves) % 10**9
        row_end = 1 + sum(row_moves) % 10**9
        print('Case #{}: {} {}'.format(t, col_end, row_end))


if __name__ == '__main__':
    robot_path_decoding()
