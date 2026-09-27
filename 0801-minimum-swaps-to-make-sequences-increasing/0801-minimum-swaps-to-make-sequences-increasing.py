class Solution:
    def minSwap(self, nums1: list[int], nums2: list[int]) -> int:
        memo  = [[-1]*2 for _ in range(len(nums1))]
        def dp(i, swap, p1, p2):
            if i == len(nums1):
                return 0

            if memo[i][swap] != -1:
                return memo[i][swap]

            ans = float('inf')
            if nums1[i] > p1 and nums2[i] > p2:
                ans = min(ans, dp(i + 1, 0, nums1[i], nums2[i]))
                
            if nums2[i] > p1 and nums1[i] > p2:
                ans = min(ans, dp(i + 1, 1, nums2[i], nums1[i]) + 1)

            memo[i][swap] = ans
            return ans

        return dp(0, 0, -1, -1)