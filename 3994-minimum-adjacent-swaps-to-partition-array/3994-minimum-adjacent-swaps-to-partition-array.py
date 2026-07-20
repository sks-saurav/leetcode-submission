class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        MOD = int(1e9) + 7

        for i, ele in enumerate(nums):
            if ele < a:
                nums[i] = 0
            elif ele > b:
                nums[i] = 2
            else:
                nums[i] = 1

        ans = 0
        count = [0] * 3
        for ele in nums:
            for i in range(ele+1, 3):
                ans =  (ans + count[i]) % MOD
            count[ele] += 1

        return ans


