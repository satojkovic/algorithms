class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        subarrays = [deque([nums[i]]) for i in range(m-1)]
        subarrays.append(deque(nums[m-1:]))
        max_sum = 0
        min_diff = sys.maxsize
        while len(subarrays[-1]) > 0:
            current_min_diff, current_max_sum = self.get_diff_and_max_sum(subarrays)
            if current_min_diff < min_diff:
                min_diff = current_min_diff
                max_sum = current_max_sum
            subarrays = self.update_subarrays(subarrays)
        return max_sum
    
    def get_diff_and_max_sum(self, subarrays):
        min_diff = sys.maxsize
        for i in range(1, len(subarrays)):
            current_sum = sum(subarrays[i])
            prev_sum = sum(subarrays[i-1])
            diff = abs(current_sum - prev_sum)
            if min_diff > diff:
                min_diff = diff
        max_sum = max([sum(subarray) for subarray in subarrays])
        return min_diff, max_sum
    
    def update_subarrays(self, subarrays):
        for i in range(1, len(subarrays)):
            move_left = subarrays[i].popleft()
            subarrays[i-1].append(move_left)
        return subarrays
        