class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)

        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1]) # rob, dont

        return dp[n-1]