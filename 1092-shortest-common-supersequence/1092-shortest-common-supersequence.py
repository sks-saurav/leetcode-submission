'''
To Saurav:
build the dp table of LCS and dry run
'''
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Phase 1: Build the DP table for LCS
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        # Phase 2: Backtrack to build the supersequence
        i, j = m, n
        res = []
        
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                res.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                res.append(str1[i - 1])
                i -= 1
            else:
                res.append(str2[j - 1])
                j -= 1
                
        # Append any remaining characters from str1
        while i > 0:
            res.append(str1[i - 1])
            i -= 1
            
        # Append any remaining characters from str2
        while j > 0:
            res.append(str2[j - 1])
            j -= 1
            
        return "".join(reversed(res))