def hanoi(N, org, work, dest):
    if N == 1:
        print('from {} to {} using {}'.format(org, dest, work))
        return
    hanoi(N-1, org, dest, work)
    hanoi(1, org, work, dest)
    hanoi(N-1, work, org, dest)

if __name__ == "__main__":
    org, work, dest = 0, 1, 2
    print('org {}, work {}, dest {}'.format(org, work, dest))
    hanoi(3, 0, 1, 2)