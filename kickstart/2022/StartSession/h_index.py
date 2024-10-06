def brute_force():
    def score(x, A):
        total = sum(A[x:])
        return total

    def calc_h_index(N, citations):
        A = [0] * (N + 1)
        ans = []
        h_index = 0
        for i in range(N):
            A[N if citations[i]>N else citations[i]] += 1
            j = i + 1
            while j and j > h_index:
                if (score(j, A) >= j):
                    h_index = j
                    break
                j -= 1
            ans.append(h_index)
        return ans

    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        citations = list(map(int, input().split()))
        h_indexes = calc_h_index(N, citations)
        print('Case #{}: '.format(t), end='')
        print(*h_indexes)


if __name__ == '__main__':
    brute_force()
