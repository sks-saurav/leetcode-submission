class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = {}

        def helper(st, end):
            if st >= end:
                return 0
            
            key = (st, end)
            if key in dp: return dp[key]
            
            ans = float('inf')

            for k in range(st, end+1):
                cost = k + max(helper(st, k-1), helper(k+1, end))
                ans = min(cost, ans)

            dp[key] = ans
            return ans


        res = helper(1, n)
        return res