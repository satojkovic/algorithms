import math
import heapq


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
        sessions = sessions[:max_diff_i] + \
            [new_excercise] + sessions[max_diff_i:]
    print('Case #: {}'.format(
        max([sessions[i] - sessions[i-1] for i in range(1, len(sessions))])))


def workout2(N, K, sessions):
    # Test Set 1: Passed
    # Test Set 2: WA
    diffs = list(
        map(lambda x: -x, [sessions[i] - sessions[i-1] for i in range(1, len(sessions))]))
    heapq.heapify(diffs)
    for k in range(K):
        if -diffs[0] == 1:
            break
        max_diff = -heapq.heappop(diffs)
        new_diff_1 = max_diff // 2
        new_diff_2 = max_diff - new_diff_1
        heapq.heappush(diffs, -new_diff_1)
        heapq.heappush(diffs, -new_diff_2)
    print('Case #: {}'.format(-diffs[0]))


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


def workout_passed():
    # Test set 1: Passed
    # Test set 2: Passed
    T = int(input())
    for t in range(1, T + 1):
        N, K = list(map(int, input().split()))
        sessions = list(map(int, input().split()))
        res = binary_search(N, K, sessions)
        print('Case #{}: {}'.format(t, res))


if __name__ == '__main__':
    workout_passed()
