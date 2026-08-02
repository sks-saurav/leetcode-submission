# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)


class TreeAncestor:
    def __init__(self, n: int, parent: list[int]):
        # The maximum number of nodes is 50,000. 
        # log2(50000) is roughly 15.6, so 17 is a safe upper bound for powers of 2.
        self.LOG = 17 
        
        # up[node][j] stores the (2^j)-th ancestor of 'node'.
        # Initialize everything to -1 (meaning no ancestor exists).
        self.up = [[-1] * self.LOG for _ in range(n)]
        
        # Base case: the 2^0 (1st) ancestor is just the direct parent.
        for i in range(n):
            self.up[i][0] = parent[i]
            
        # DP transition: fill the table for powers of 2
        for j in range(1, self.LOG):
            for i in range(n):
                # If the node has a 2^(j-1)-th ancestor...
                if self.up[i][j-1] != -1:
                    # The 2^j-th ancestor is the 2^(j-1)-th ancestor OF the 2^(j-1)-th ancestor.
                    self.up[i][j] = self.up[ self.up[i][j-1] ][ j-1 ]

    def getKthAncestor(self, node: int, k: int) -> int:
        # Iterate through the bit positions (0 to 16)
        for j in range(self.LOG):
            # If the j-th bit of k is set to 1, we need to jump 2^j steps
            if (k & (1 << j)) > 0:
                node = self.up[node][j]
                
                # If we overshoot the root, we've hit a non-existent ancestor
                if node == -1:
                    break
                    
        return node