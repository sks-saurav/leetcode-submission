class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * n

        for i in range(n-1, -1, -1):
            if nums[i] == 1:
                dp[i] = 1 + (dp[i+1] if i+1 < n else 0)

        ans = max(dp)-1
        ll = 0
        for i in range(n):
            if nums[i] == 0:
                rr = dp[i+1] if i+1 < n else 0
                ans = max(ans, ll + rr)
                ll = 0
            else:
                ll += 1

        return ans
            


        