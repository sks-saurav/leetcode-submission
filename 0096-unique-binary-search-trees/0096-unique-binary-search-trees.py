class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 1
            
        # Create an (n+2) x (n+2) matrix to safely access k-1 and k+1
        # 1-indexed to match values 1 through n naturally
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        
        # Base Case 1: Empty trees (i > j).
        # If the left or right subtree is empty, it counts as 1 valid structure.
        for i in range(1, n + 2):
            for j in range(0, i):
                dp[i][j] = 1
                
        # Base Case 2: Single nodes (i == j).
        # A single node forms exactly 1 valid tree structure.
        for i in range(1, n + 1):
            dp[i][i] = 1
            
        # MCM Pattern: Iterate by the length of the interval
        for length in range(2, n + 1):
            for i in range(1, n - length + 2):
                j = i + length - 1  # The end of our current interval
                
                # Pick every node k in the interval [i, j] to be the root
                for k in range(i, j + 1):
                    left_subtrees = dp[i][k - 1]
                    right_subtrees = dp[k + 1][j]
                    
                    dp[i][j] += left_subtrees * right_subtrees
                    
        # Return the answer for the full sequence from 1 to n
        return dp[1][n]