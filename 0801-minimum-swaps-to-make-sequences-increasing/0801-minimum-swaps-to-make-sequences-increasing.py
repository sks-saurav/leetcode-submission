class Solution:
    def minSwap(self, nums1: list[int], nums2: list[int]) -> int:
        # Base cases for index 0
        not_swap = 0
        swap = 1
        
        for i in range(1, len(nums1)):
            curr_not_swap = float('inf')
            curr_swap = float('inf')
            
            # Condition 1: Straight check (ordered without crossing)
            if nums1[i-1] < nums1[i] and nums2[i-1] < nums2[i]:
                curr_not_swap = not_swap             # No swap previous -> No swap current
                curr_swap = swap + 1                 # Swap previous -> Swap current
                
            # Condition 2: Cross check (ordered by crossing)
            if nums1[i-1] < nums2[i] and nums2[i-1] < nums1[i]:
                curr_not_swap = min(curr_not_swap, swap)         # Swap previous -> No swap current
                curr_swap = min(curr_swap, not_swap + 1)         # No swap previous -> Swap current
                
            # Move current state to previous state for the next iteration
            not_swap, swap = curr_not_swap, curr_swap
            
        return min(not_swap, swap)

# class Solution:
#     def minSwap(self, nums1: list[int], nums2: list[int]) -> int:
#         n1 = [-1] + nums1
#         n2 = [-1] + nums2

#         dp = [[float('inf')]*2 for _ in range(len(n1))]
#         dp[0][0] = dp[0][1] = 0

#         for i in range(1, len(n1)):
#             # no pvs swap
#             p1, p2 = n1[i-1], n2[i-1]
#             if p1 < n1[i] and p2 < n2[i]:
#                 dp[i][0] = min(dp[i][0], dp[i-1][0])

#             if p1 < n2[i] and p2 < n1[i]:
#                 dp[i][1] = min(dp[i][1], 1 + dp[i-1][0])

#             # pvs swap
#             p1, p2 = n2[i-1], n1[i-1]
#             if p1 < n1[i] and p2 < n2[i]:
#                 dp[i][0] = min(dp[i][0], dp[i-1][1])

#             if p1 < n2[i] and p2 < n1[i]:
#                 dp[i][1] = min(dp[i][1], 1 + dp[i-1][1])

#         n = len(n1)
#         return min(dp[n-1][0], dp[n-1][1])



# class Solution:
#     def minSwap(self, nums1: list[int], nums2: list[int]) -> int:
#         memo  = [[-1]*2 for _ in range(len(nums1))]
#         def dp(i, swap, p1, p2):
#             if i == len(nums1):
#                 return 0

#             if memo[i][swap] != -1:
#                 return memo[i][swap]

#             ans = float('inf')
#             if nums1[i] > p1 and nums2[i] > p2:
#                 ans = min(ans, dp(i + 1, 0, nums1[i], nums2[i]))
                
#             if nums2[i] > p1 and nums1[i] > p2:
#                 ans = min(ans, dp(i + 1, 1, nums2[i], nums1[i]) + 1)

#             memo[i][swap] = ans
#             return ans

#         return dp(0, 0, -1, -1)