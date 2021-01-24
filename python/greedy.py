def scheduling(intervals):
    reqs = sorted(intervals, key=lambda x: x[1])
    ans = []
    current_end = 0
    for i in range(len(reqs)):
        if current_end <= reqs[i][0]:
            ans.append(reqs[i])
            current_end = reqs[i][1]
    return ans

if __name__ == "__main__":
    intervals = [[9, 16], [10, 12], [11, 15], [13, 19], [15, 18], [19, 23]]
    print(scheduling(intervals))
