class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        ## BOTTOM UP
        dp = [0, float('-inf'), float('-inf')]

        for num in nums:
            next_dp = dp[:]
            
            for rem in range(3):
                next_rem = (rem + num) % 3
                next_dp[next_rem] = max(next_dp[next_rem], dp[rem] + num)
            
            dp = next_dp

        return dp[0]


        ## MEMOIZATION
        # @cache
        # def helper(idx, rem):
        #     if idx < 0:
        #         return 0 if rem == 0 else float('-inf')

        #     ans = float('-inf')
        #     ans = max(ans, helper(idx-1, (rem - nums[idx]) % 3) + nums[idx])
        #     ans = max(ans, helper(idx-1, rem))

        #     return ans

        # return helper(len(nums)-1, 0)