class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''  
        sum(P) - sum(N) = target
        sum(P) + sum(N) = totalSum
       
        sum(P) = (target + totalSum) / 2

        Peduced to finding the number of ways to form subset with the sum = (target + totalSum) / 2
        '''
        total_sum = sum(nums)
        if abs(target) > total_sum or (total_sum + target) % 2 != 0:
            return 0
        
        target_ss = (total_sum + target) // 2
        n = len(nums)
        dp = [0] * (target_ss + 1)
        dp[0] = 1 
       
            
        for i in range(n):
            val = nums[i]
            for j in range(target_ss, val-1, -1):
                dp[j] = dp[j] + dp[j - val]

        return dp[target_ss]
     



        