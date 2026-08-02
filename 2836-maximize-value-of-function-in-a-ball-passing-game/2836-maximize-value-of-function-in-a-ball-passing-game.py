class Solution:
    def getMaxFunctionValue(self, receiver: list[int], k: int) -> int:
        # Here k is up to 10^10, log2(10^10) is ~33.2, so 35 is a safe upper bound
        maxD = 35
        n = len(receiver)
        
        # kthParent[i][j] will store the (2^j)-th step from node i
        kthParent = [[0] * maxD for _ in range(n)]
        
        # cost[i][j] will store the sum of node values along the path of 2^j steps starting from node i
        cost = [[0] * maxD for _ in range(n)]
        
        # Precompute the tables
        for i in range(maxD):
            for j in range(n):
                if i == 0:
                    kthParent[j][i] = receiver[j]
                    cost[j][i] = receiver[j]
                else:
                    kthParent[j][i] = kthParent[ kthParent[j][i-1] ][i-1]
                    
                    # Accumulate sum for 2^i steps: 
                    # Sum of first 2^(i-1) steps + Sum of next 2^(i-1) steps from the midpoint
                    cost[j][i] = cost[j][i-1] + cost[ kthParent[j][i-1] ][i-1]
        
        ans = 0
        
        # Evaluate the maximum path sum of exactly k steps starting from each node
        for i in range(n):
            # The starting node's value is always included in the sum initially
            sum_val = i 
            node = i
            
            for j in range(maxD):
                # Check if the j-th bit of k is set
                if (1 << j) & k:
                    # Use 'node' instead of 'i' because the current node shifts as we make jumps
                    sum_val += cost[node][j]
                    node = kthParent[node][j]
            
            # Keep track of the maximum sum found across all starting nodes
            ans = max(ans, sum_val)
            
        return ans        