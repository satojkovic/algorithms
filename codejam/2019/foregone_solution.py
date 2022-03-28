def decompose_four(num):
    A = list(num)
    B = ['0'] * len(A)
    for i in range(len(A)):
        if A[i] == '4':
            A[i] = '2'
            B[i] = '2'
    A = ''.join(A)
    B = ''.join(B).lstrip('0')
    return A, B


T = int(input())
for t in range(1, T + 1):
    num = input().strip()
    A, B = decompose_four(num)
    print("Case #{}: {} {}".format(t, A, B))
