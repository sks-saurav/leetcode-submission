class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for index, num in enumerate(nums):            
            other = target - num
            
            if other in prev:
                return [prev[other], index]

            prev[num] = index

        return []