def workout(N, K, sessions):
    # Test Set 1: Passed
    # Test Set 2: TLE
    for k in range(K):
        diffs = [sessions[i] - sessions[i-1] for i in range(1, len(sessions))]
        max_diff = max(diffs)
        if max_diff == 1:
            break
        max_diff_i = diffs.index(max_diff) + 1
        new_excercise = (sessions[max_diff_i] + sessions[max_diff_i - 1]) // 2
        sessions = sessions[:max_diff_i] + [new_excercise] + sessions[max_diff_i:]
    print('Case #: {}'.format(max([sessions[i] - sessions[i-1] for i in range(1, len(sessions))])))

import math
def check(N, K, sessions, mid):
    additional_session = 0
    for i in range(1, N):
        additional_session += math.ceil((sessions[i] - sessions[i-1])/mid) - 1
    return True if additional_session <= K else False

def binary_search(N, K, sessions):
    def _binary_search(left, right):
        while left < right:
            mid = (left + right) // 2
            if check(N, K, sessions, mid):
                right = mid
            else:
                left = mid + 1
        return left
    return _binary_search(1, 10**9-1)

def workout_passed(N, K, sessions):
    # Test set 1: Passed
    # Test set 2: Passed
    res = binary_search(N, K, sessions)
    print('Case #: {}'.format(res))

if __name__ == '__main__':
    N, K = 5, 2
    sessions = [10, 13, 15, 16, 17]
    workout_passed(N, K, sessions)
    
