from collections import Counter, deque
from typing import List
import heapq

def leastInterval(tasks: List[str], n: int) -> int:
    counts = Counter(tasks)
    task_freqs = [(-freq, label) for label, freq in counts.items()]
    heapq.heapify(task_freqs)

    time = 0
    wait_queue = deque()
    while task_freqs or wait_queue:
        while wait_queue and wait_queue[0][1] <= time:
            task_to_return = wait_queue.popleft()
            heapq.heappush(task_freqs, task_to_return[0])
        if task_freqs:
            freq, label = heapq.heappop(task_freqs)
            freq += 1
            if freq < 0:
                wait_queue.append(((freq, label), time + n + 1))

        time += 1

    return time


def test_least_interval():
    assert leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert leastInterval(["A", "A", "A", "B", "B", "B"], 0) == 6
    assert leastInterval(["A", "A", "A", "A", "B", "B", "C", "C"], 2) == 10
