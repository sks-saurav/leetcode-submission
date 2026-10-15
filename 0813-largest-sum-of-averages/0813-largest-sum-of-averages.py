# class Solution:
#     def largestSumOfAverages(self, nums: list[int], k: int) -> float:
#         n = len(nums)
#         psum = [0] * (n + 1)
#         for i in range(n):
#             psum[i + 1] = psum[i] + nums[i]

#         @cache
#         def helper(idx: int, rem_k: int) -> float:
#             # If we reached the end, no more score to collect
#             if idx == n:
#                 return 0.0

#             # If only 1 partition remaining, we MUST take the rest of the array
#             if rem_k == 1:
#                 return (psum[n] - psum[idx]) / (n - idx)

#             # Option A: Take all remaining elements as 1 group (allowed since it's "at most k")
#             best = (psum[n] - psum[idx]) / (n - idx)

#             # Option B: End current subarray at j, and recurse for the rest with rem_k - 1
#             for j in range(idx, n - 1):
#                 cur_avg = (psum[j + 1] - psum[idx]) / (j - idx + 1)
#                 best = max(best, cur_avg + helper(j + 1, rem_k - 1))

#             return best

#         return helper(0, k)


class Solution:
    def largestSumOfAverages(self, nums: list[int], k: int) -> float:
        n = len(nums)
        psum = [0] * (n + 1)
        for i in range(n):
            psum[i + 1] = psum[i] + nums[i]

        # dp[c][i]: max score using at most c partitions for prefix nums[:i]
        dp = [[0.0] * (n + 1) for _ in range(k + 1)]

        # Base case: 1 partition -> full prefix average
        for i in range(1, n + 1):
            dp[1][i] = psum[i] / i

        # Transitions for 2 to k partitions
        for c in range(2, k + 1):
            for i in range(c, n + 1):
                # We can always carry forward the result using fewer partitions
                dp[c][i] = dp[c - 1][i]
                for j in range(c - 1, i):
                    subarray_avg = (psum[i] - psum[j]) / (i - j)
                    dp[c][i] = max(dp[c][i], dp[c - 1][j] + subarray_avg)

        return dp[k][n]