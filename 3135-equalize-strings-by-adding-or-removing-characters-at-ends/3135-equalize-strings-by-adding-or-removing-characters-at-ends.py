# PREMIUM

class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        n, m = len(initial), len(target)
        
        # dp[i][j] stores the length of the longest common suffix 
        # for the prefixes initial[0..i-1] and target[0..j-1]
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        max_len = 0
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # If the characters match, extend the previous diagonal match
                if initial[i - 1] == target[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(max_len, dp[i][j])
                else:
                    # If they don't match, the continuous string is broken
                    dp[i][j] = 0
                    
        # Total operations = Deletions + Additions
        return (n - max_len) + (m - max_len)