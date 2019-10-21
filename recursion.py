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