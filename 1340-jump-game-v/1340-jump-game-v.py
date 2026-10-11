class Solution:
    def maxJumps(self, arr: list[int], d: int) -> int:
        n = len(arr)
        dp = [1] * n

        # Sort indices by their value in ascending order
        sorted_indices = sorted(range(n), key=lambda i: arr[i])

        for idx in sorted_indices:
            # Jump right
            for j in range(idx + 1, min(n, idx + d + 1)):
                if arr[j] >= arr[idx]:
                    break
                dp[idx] = max(dp[idx], 1 + dp[j])

            # Jump left
            for j in range(idx - 1, max(-1, idx - d - 1), -1):
                if arr[j] >= arr[idx]:
                    break
                dp[idx] = max(dp[idx], 1 + dp[j])

        return max(dp)

# class Solution:
#     def maxJumps(self, arr: list[int], d: int) -> int:
#         @cache
#         def helper(idx):
#             ans = 1
#             i = idx+1
#             while i < len(arr) and i <= idx+d and arr[idx] > arr[i]:
#                 ans = max(ans, 1 + helper(i))
#                 i += 1
            
#             i = idx-1
#             while i >= 0 and i >= idx-d and arr[idx] > arr[i]:
#                 ans = max(ans, 1+helper(i))
#                 i -= 1

#             return ans

#         result = 0
#         for i in range(len(arr)):
#             result = max(result, helper(i))

#         return result
