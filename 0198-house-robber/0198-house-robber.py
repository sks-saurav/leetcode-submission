class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        # dp[i][0] -> skip house i
        # dp[i][1] -> rob house i
        dp = [[0] * 2 for _ in range(n)]

        dp[0][0] = 0
        dp[0][1] = nums[0]

        for i in range(1, n):
            # If you skip house i, the previous house could have been robbed OR skipped. You want the best of both worlds.
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])

            # If you rob house i, house i - 1 MUST have been skipped.
            dp[i][1] = dp[i - 1][0] + nums[i]

        return max(dp[n - 1][0], dp[n - 1][1])