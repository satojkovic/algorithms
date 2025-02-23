from collections import defaultdict


class TimeMapLinear:

    def __init__(self):
        self.data = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        timestamp_prev = timestamp
        while timestamp_prev >= 1:
            if timestamp_prev in self.data[key]:
                return self.data[key][timestamp_prev]
            timestamp_prev -= 1
        return ""


class TimeMap:

    def __init__(self):
        self.data = defaultdict(dict)
        self.key_timestamp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key][timestamp] = value
        self.key_timestamp[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        left, right = 0, len(self.key_timestamp[key]) - 1
        target_timestamp = self.key_timestamp[key][-1]
        while left <= right:
            mid = left + (right - left) // 2
            if self.key_timestamp[key][mid] == timestamp:
                target_timestamp = self.key_timestamp[key][mid]
                return self.data[key][target_timestamp]
            elif self.key_timestamp[key][mid] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        return self.data[key][self.key_timestamp[key][right]] if right >= 0 else ""


def test_timemap():
    tm = TimeMapLinear()
    tm.set("foo","bar",1)
    assert tm.get("foo", 1) == "bar"
    assert tm.get("foo", 3) == "bar"
    tm.set("foo","bar2",4)
    assert tm.get("foo", 4) == "bar2"
    assert tm.get("foo", 5) == "bar2"

    tm = TimeMap()
    tm.set("foo","bar",1)
    assert tm.get("foo", 1) == "bar"
    assert tm.get("foo", 3) == "bar"
    tm.set("foo","bar2",4)
    assert tm.get("foo", 4) == "bar2"
    assert tm.get("foo", 5) == "bar2"
