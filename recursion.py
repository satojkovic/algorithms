def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

def fib_memo(n):
    def fib_m(n, memo):
        if n == 0 or n == 1:
            return n

        if memo[n] == 0:
            memo[n] = fib_m(n - 1) + fib_m(n - 2)
        return memo[n]

    # memoization of (n + 1) values (from 0 to n)
    memo = (n + 1) * [0]
    return fib_m(n, memo)

def reverse_str(s):
    if len(s) == 0:
        return s
    rstr = reverse_str(s[1:])
    return ''.join([rstr, s[0]])

def reverse_str2(s):
    if len(s) == 0:
        return []
    rstr = reverse_str2(s[1:])
    return rstr + [s[0]]

def reverse_str3(s, head, tail):
    if head >= tail:
        return
    s[head], s[tail] = s[tail], s[head]
    return reverse_str3(s, head + 1, tail - 1)

def swap_node_pairs(head):
    if head is None or head.next_elem is None:
        return head
    swap_head = swap_node_pairs(head.next_elem.next_elem)
    pair = head.next_elem
    head.next_elem = swap_head
    pair.next_elem = head
    return pair

def climb_stairs(n):
    def cs_memo(n, memo):
        if n < 0:
            return 0
        elif n == 0:
            return 1

        if memo[n] == 0:
            memo[n] = cs_memo(n - 1, memo) + cs_memo(n - 2, memo)
        return memo[n]

    memo = (n + 1) * [0]
    return cs_memo(n, memo)

def pascal_triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [n * [1]]
    prev_rows = pascal_triangle(n - 1)
    cur_row = n * [1]
    for i in range(n):
        if i == 0 or i == n - 1:
            continue
        cur_row[i] = prev_rows[n - 2][i - 1] + prev_rows[n - 2][i]
    prev_rows.append(cur_row)
    return prev_rows

def pascal_triangle2(n):
    if n == 0:
        return [1]
    elif n == 1:
        return (n+1) * [1]
    prev_row = pascal_triangle2(n - 1)
    cur_row = (n+1) * [1]
    for i in range(n+1):
        if i == 0 or i == n:
            continue
        cur_row[i] = prev_row[i - 1] + prev_row[i]
    return cur_row

def pascal_triangle3(n):
    if n == 0:
        return [1]
    elif n == 1:
        return (n+1) * [1]
    prev_row = pascal_triangle2(n - 1)
    for i in reversed(range(1, n)):
        prev_row[i] = prev_row[i - 1] + prev_row[i]
    return prev_row + [1]

def reverse_list(head):
    if not head or head.next_elem is None:
        return head
    node = reverse_list(head.next_elem)
    head.next_elem.next_elem = head
    head.next_elem = None
    return node

def max_depth(root):
    def helper(root, depth):
        if root is None:
            return depth - 1
        return max(helper(root.left, depth + 1), helper(root.right, depth + 1))
    return helper(root, 0)

def pow(x, n):
    if n == 0:
        return 1
    return x * pow(x, n - 1) if n > 0 else (1/x) * pow(x, n + 1)

def pow2(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x

    if n > 0:
        return pow2(x, n // 2) * pow2(x, n - n // 2)
    else:
        n = abs(n)
        return pow2(1 / x, n // 2) * pow2(1 / x, n - n // 2)

def pow3(x, n):
    def helper(x, n, memo):
        if n == 0:
            return 1
        elif n == 1:
            return x

        if memo[abs(n)] < 0:
            if n > 0:
                memo[n] = helper(x, n // 2, memo) * helper(x, n - n // 2, memo)
            else:
                n = abs(n)
                memo[n] = helper(1 / x, n // 2, memo) * helper(1 / x, n - n // 2, memo)
        return memo[n]
    memo = (abs(n) + 1) * [-1]
    return helper(x, n, memo)

def pow4(x, n):
    def helper(x, n, memo):
        if n == 0:
            return 1
        elif n == 1:
            return x

        if memo.get(abs(n)) is None:
            if n > 0:
                memo[n] = helper(x, n // 2, memo) * helper(x, n - n // 2, memo)
            else:
                n = abs(n)
                memo[n] = helper(1 / x, n // 2, memo) * helper(1 / x, n - n // 2, memo)
        return memo[n]
    memo = {}
    return helper(x, n, memo)

def kth_symbol(N, K):
    def n_row(N):
        if N == 1:
            return 0
        row = n_row(N - 1)
        bits = format(row, 'b').zfill(2 ** (N - 2))
        i_bits = ''.join(['1' if x == '0' else '0' for x in bits])
        return int(bits + i_bits, 2)
    row = n_row(N)
    return 1 if (row & (1 << (2 ** (N - 1) - K))) else 0

def kth_symbol2(N, K):
    if N == 1:
        return 0
    symbol = kth_symbol2(N - 1, (K - 1) % (2 ** (N -2)) + 1)
    if K > (2 ** N - 2):
        return 0 if symbol == 1 else 1
    else:
        return 0 if symbol == 1 else 1

def perm(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    res = []
    for p in perm(n - 1):
        for i in range(n):
            res.append(p[:i] + [n] + p[i:])
    return res

def search_2d_mat(mat, target):
    M, N = len(mat), len(mat[0])
    return search(mat, target, 0, 0, M - 1, N - 1)

def search(mat, target, top, left, bottom, right):
    if top * len(mat[0]) + left > bottom * len(mat[0]) + right:
        return False
    mid_row = (top + bottom) // 2
    mid_col = (left + right) // 2
    if mat[mid_row][mid_col] == target:
        return True
    # Check top-left sub matrix recursively
    if search(mat, target, top, left, mid_row, mid_col):
        return True
    # Check top-right sub matrix recursively
    if search(mat, target, top, mid_col, mid_row, right):
        return True
    # Check bottom-left sub matrix recursively
    if search(mat, target, mid_row, left, bottom, mid_col):
        return True
    # Check bottom-right sub matrix recursively
    if search(mat, target, mid_row, mid_col, bottom, right):
        return True
    # All conditions are False, then return False
    return False