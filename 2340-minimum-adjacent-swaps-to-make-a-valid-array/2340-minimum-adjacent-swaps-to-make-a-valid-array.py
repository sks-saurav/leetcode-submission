# PREMIUM
class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        min_ele = min(nums)
        max_ele = max(nums)
        min_idx, max_idx = n-1, 0

        for i in range(n):
            if nums[i] == min_ele:
                min_idx = i
                break

        for i in range(n-1, -1, -1):
            if nums[i] == max_ele:
                max_idx = i
                break

        ans = min_idx + (n-max_idx-1)
        if max_idx < min_idx:
            ans -= 1

        return ans