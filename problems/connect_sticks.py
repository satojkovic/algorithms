def connect_sticks(sticks):
    import heapq
    heapq.heapify(sticks)
    ret = 0
    while len(sticks) > 1:
        x, y = heapq.heappop(sticks), heapq.heappop(sticks)
        ret += (x + y)
        heapq.heappush(sticks, x + y)
    return ret

if __name__ == "__main__":
    print(connect_sticks([2, 4, 3])) # 14