class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0
        
        m, n = len(mat), len(mat[0])
        # dp[i][j] stores [horizontal, vertical, diagonal, anti-diagonal]
        dp = [[[0] * 4 for _ in range(n)] for _ in range(m)]
        max_len = 0
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    # 0: Horizontal (left to right)
                    dp[i][j][0] = (dp[i][j - 1][0] if j > 0 else 0) + 1
                    
                    # 1: Vertical (top to bottom)
                    dp[i][j][1] = (dp[i - 1][j][1] if i > 0 else 0) + 1
                    
                    # 2: Diagonal (top-left to bottom-right)
                    dp[i][j][2] = (dp[i - 1][j - 1][2] if i > 0 and j > 0 else 0) + 1
                    
                    # 3: Anti-diagonal (top-right to bottom-left)
                    dp[i][j][3] = (dp[i - 1][j + 1][3] if i > 0 and j < n - 1 else 0) + 1
                    
                    max_len = max(max_len, max(dp[i][j]))
                    
        return max_len