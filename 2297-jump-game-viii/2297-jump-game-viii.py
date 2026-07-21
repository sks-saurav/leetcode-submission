# PREMIUM
class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        n = len(nums)
        higher = [-1] * n
        lower = [-1] * n

        stack1 = []
        stack2 = []
        for i in range(n):
            while stack1 and nums[stack1[-1]] <= nums[i]:
                higher[stack1[-1]] = i
                stack1.pop()
            stack1.append(i)

            while stack2 and nums[stack2[-1]] > nums[i]:
                lower[stack2[-1]] = i
                stack2.pop()
            stack2.append(i)

        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(n):
            n1, n2 = higher[i], lower[i]
            if n1 != -1:
                dp[n1] = min(dp[i] + costs[n1], dp[n1])
            if n2 != -1:
                dp[n2] = min(dp[i] + costs[n2], dp[n2])

        return dp[n-1]



