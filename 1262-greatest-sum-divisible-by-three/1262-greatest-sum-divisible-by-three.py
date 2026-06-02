class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        
        @cache
        def helper(idx, rem):
            if idx < 0:
                return 0 if rem == 0 else float('-inf')

            ans = float('-inf')
            ans = max(ans, helper(idx-1, (rem - nums[idx]) % 3) + nums[idx])
            ans = max(ans, helper(idx-1, rem))

            return ans

        return helper(len(nums)-1, 0)