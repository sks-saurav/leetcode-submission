class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lidx = bisect_left(nums, target)

        if lidx >= len(nums) or nums[lidx] != target:
            return [-1, -1]

        
        ridx = bisect_right(nums, target)
        return [lidx, ridx-1]