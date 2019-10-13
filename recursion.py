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