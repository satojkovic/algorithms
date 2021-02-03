def scheduling(intervals):
    reqs = sorted(intervals, key=lambda x: x[1])
    ans = []
    current_end = 0
    for i in range(len(reqs)):
        if current_end <= reqs[i][0]:
            ans.append(reqs[i])
            current_end = reqs[i][1]
    return ans

def multiple_array(A, B):
    N = len(A)
    total = 0
    for i in range(N - 1, -1 , -1):
        A[i] += total
        count = 0 if A[i] % B[i] == 0 else B[i] - (A[i] % B[i])
        total += count
    return total

if __name__ == "__main__":
    intervals = [[9, 16], [10, 12], [11, 15], [13, 19], [15, 18], [19, 23]]
    print(scheduling(intervals))
