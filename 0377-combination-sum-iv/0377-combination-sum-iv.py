class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        n = len(nums)
        dp = [0] * (target+1)
        dp[0] = 1

        for val in range(1, target+1):
            for i in range(n):
                if val-nums[i] >= 0:
                    dp[val] += dp[val-nums[i]]

        return dp[target]
