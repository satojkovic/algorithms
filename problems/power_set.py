def power_set(S):
    def helper(S, i):
        if len(S[i:]) == 0:
            return [[]]
        ps = []
        for sub_ps in helper(S, i+1):
            ps.append(sub_ps)
            ps.append(sub_ps + [S[i]])
        return ps
    return helper(S, 0)

if __name__ == "__main__":
    ps = power_set(['a', 'b', 'c'])
    print(ps)