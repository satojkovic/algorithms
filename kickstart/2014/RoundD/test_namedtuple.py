def solve():
    from collections import namedtuple
    Pair = namedtuple('Pair', ['first', 'second'])

    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        ticket_list = [Pair(input(), input()) for _ in range(N)]
        for ticket in ticket_list:
            print(ticket.first, ticket.second)


if __name__ == '__main__':
    solve()
