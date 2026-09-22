class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        # Optimization: standardize orientation to reduce state space
        if n > m:
            n, m = m, n
            
        ans = n * m  # Maximum possible squares (all 1x1)
        memo = {}
        
        def dfs(skyline, count):
            nonlocal ans
            
            # Prune: if we already used too many squares
            if count >= ans:
                return
                
            # Prune: if we've seen this skyline with fewer or equal squares
            if skyline in memo and memo[skyline] <= count:
                return
            memo[skyline] = count
            
            min_h = min(skyline)
            
            # Base case: if the lowest height is n, the board is perfectly filled
            if min_h == n:
                ans = count
                return
                
            # Find the leftmost column with this minimum height
            c = skyline.index(min_h)
            
            # Find the maximum valid square we can place here
            max_k = 1
            while (c + max_k < m and 
                   skyline[c + max_k] == min_h and 
                   min_h + max_k < n):
                max_k += 1
                
            # Greedily try larger squares first to establish a tight bound for pruning
            for k in range(max_k, 0, -1):
                # Create the new state
                next_skyline = list(skyline)
                for i in range(c, c + k):
                    next_skyline[i] += k
                    
                dfs(tuple(next_skyline), count + 1)
                
        # Initial state: m columns, all at height 0
        dfs((0,) * m, 0)
        
        return ans