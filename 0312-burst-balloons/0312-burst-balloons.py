class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for l in range(3, n+1):
            for st in range(n-l+1):
                end = st+l-1

                for k in range(st+1, end):
                    cost = nums[st] * nums[k] * nums[end]
                    dp[st][end] = max(dp[st][end], cost + dp[st][k] + dp[k][end])

        return dp[0][n-1]

# class Solution:
#     '''
#     Think backword, what baloon will remain last, then second last and so on...
#     https://www.youtube.com/watch?v=Yz4LlDSlkns&list=PLgUwDviBIf0pwFf-BnpkXxs0Ra0eU2sJY&index=25
#     '''
#     def maxCoins(self, nums: List[int]) -> int:
#         arr = [1] + nums + [1]
#         dp = {}

#         def helper(st, end):
#             if end - st <= 1:
#                 return 0

#             key = (st, end)
#             if key in dp: return dp[key]

#             ans = 0
            
#             for k in range(st+1, end):
#                 temp_cost = arr[st] * arr[k] * arr[end]
#                 cost = helper(st, k) +  helper(k, end) + temp_cost
#                 ans = max(ans, cost)

#             dp[key] = ans
#             return ans

#         return helper(0, len(arr)-1)
