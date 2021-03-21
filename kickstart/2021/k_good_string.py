# Test set1: Passed
# Test set2: Passed
def k_good_string():
    T = int(input())
    for t in range(1, T + 1):
        N, K = list(map(int, input().split()))
        S = input()
        k = 0
        for i in range(N//2):
            if S[i] != S[N-i-1]:
                k += 1
        print('Case #{}: {}'.format(t, max(0, K - k)))

if __name__ == '__main__':
    k_good_string()
