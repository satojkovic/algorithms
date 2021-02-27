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

if __name__ == '__main__':
    N, K = 5, 2
    sessions = [10, 13, 15, 16, 17]
    workout(N, K, sessions)
    
