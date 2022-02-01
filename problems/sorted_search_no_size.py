class Listy:
    def __init__(self, nums=None):
        self.nums = nums if nums else []
        self.nums.sort()

    def element_at(self, index):
        if index < len(self.nums):
            return self.nums[index]
        else:
            return -1

    def search(self, target):
        index = 1
        while self.element_at(index) != -1 and self.element_at(index) < target:
            index *= 2
        return self._binary_search(target, index // 2, index)

    def _binary_search(self, target, left, right):
        while left <= right:
            mid = left + (right - left) // 2
            if self.element_at(mid) == -1 or self.nums[mid] > target:
                right = mid - 1
            elif self.nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1


def test_sorted_search_no_size():
    listy = Listy([1, 3, 7, 8, 11])
    assert listy.search(8) == 3
    assert listy.search(11) == 4
    assert listy.search(1) == 0
    assert listy.search(15) == -1
    assert listy.search(2) == -1
