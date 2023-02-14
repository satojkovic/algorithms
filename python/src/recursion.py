def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)


def fib_memo(n):
    def fib_m(n, memo):
        if n == 0 or n == 1:
            return n
        if memo[n] == -1:
            memo[n] = fib_m(n - 1, memo) + fib_m(n - 2, memo)
        return memo[n]

    # memoization of (n + 1) values (from 0 to n)
    memo = (n + 1) * [-1]
    return fib_m(n, memo)


def trib_memo(n):
    def trib_m(n, memo):
        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1
        if memo[n] == -1:
            memo[n] = trib_m(n-3, memo) + trib_m(n-2, memo) + trib_m(n-1, memo)
        return memo[n]

    memo = (n + 1) * [-1]
    return trib_m(n, memo)


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
    if head is None or head.next is None:
        return head
    swap_head = swap_node_pairs(head.next.next)
    pair = head.next
    head.next = swap_head
    pair.next = head
    return pair


def climb_stairs(n):
    def cs_memo(n, memo):
        if n == 0 or n == 1:
            return 1
        if memo[n] == -1:
            memo[n] = cs_memo(n - 1, memo) + cs_memo(n - 2, memo)
        return memo[n]

    memo = (n + 1) * [-1]
    return cs_memo(n, memo)


def climb_stairs_dp(n):
    if n == 0 or n == 1:
        return 1
    dp = (n + 1) * [0]
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


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
    if head is None or head.next is None:
        return head
    node = reverse_list(head.next)
    head.next.next = head
    head.next = None
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
                memo[n] = helper(1 / x, n // 2, memo) * \
                    helper(1 / x, n - n // 2, memo)
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
                memo[n] = helper(1 / x, n // 2, memo) * \
                    helper(1 / x, n - n // 2, memo)
        return memo[n]
    memo = {}
    return helper(x, n, memo)


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
    if len(mat) == 0 or len(mat[0]) == 0:
        return False
    M, N = len(mat), len(mat[0])
    return search(mat, target, 0, 0, M - 1, N - 1)


def search(mat, target, top, left, bottom, right):
    # Area size is zero
    if top > bottom or left > right:
        return False
    # Target doesn't exist in this area
    elif mat[top][left] > target or mat[bottom][right] < target:
        return False

    # Search row such that mat[row - 1][mid_col] < target mat[row][mid_col]
    # because target should exist somewhere in the bottom-left area or top-right area
    mid_col = left + (right - left) // 2
    row = top
    while row <= bottom and mat[row][mid_col] <= target:
        if mat[row][mid_col] == target:
            return True
        row += 1
    return search(mat, target, row, left, bottom, mid_col - 1) or search(mat, target, top, mid_col + 1, row - 1, right)
