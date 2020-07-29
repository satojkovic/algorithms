from collections import Counter
from heapq import heapify, heappop, heappush
def rearrange_str(s):
    counter = Counter(s)
    pq = [(-freq, char) for char, freq in counter.items()]
    heapify(pq)
    prev_char, prev_freq = '', 0
    res = []
    while pq:
        freq, char = heappop(pq)
        res.append(char)
        if prev_freq < 0:
            heappush(pq, (prev_freq, prev_char))
        prev_freq = freq + 1
        prev_char = char
    return ''.join(res) if len(res) == len(s) else ''
