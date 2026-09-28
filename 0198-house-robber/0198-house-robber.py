class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)

        # dp[i][0] -> money when not robbed ith house
        # dp[i][1] -> money when robbed the ith house
        dp = [[0] * 2 for _ in range(n)]
        
        dp[0][0] = 0
        dp[0][1] = nums[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = max(dp[i-1][0] + nums[i], dp[i-1][1])

        return max(dp[n-1][0], dp[n-1][1])