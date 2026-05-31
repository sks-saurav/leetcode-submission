class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        dp[n] = 1

        for idx in range(n-1, -1, -1):
            dig1 = ord(s[idx]) - ord('0')
            ways = 0
            if dig1 != 0:
                ways = dp[idx+1]

            if idx+1 < len(s):
                dig2 = ord(s[idx+1]) - ord('0')

                if dig1 == 1:
                    ways += dp[idx+2]
                elif dig1 == 2 and dig2 <= 6:
                    ways += dp[idx+2]
            
            dp[idx] = ways

        return dp[0]

        
        # @cache
        # def helper(idx):
        #     if idx == len(s):
        #         return 1

        #     dig1 = ord(s[idx]) - ord('0')

        #     ways = 0
        #     if dig1 != 0:
        #         ways = helper(idx+1)

        #     if idx+1 < len(s):
        #         dig2 = ord(s[idx+1]) - ord('0')

        #         if dig1 == 1:
        #             ways += helper(idx+2)
        #         elif dig1 == 2 and dig2 <= 6:
        #             ways += helper(idx+2)

        #     return ways

        # return helper(0)
