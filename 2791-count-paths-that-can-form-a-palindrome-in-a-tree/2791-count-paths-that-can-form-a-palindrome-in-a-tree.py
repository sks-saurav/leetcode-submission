class Solution:
    def countPalindromePaths(self, parent: list[int], s: str) -> int:
        n = len(parent)
        adj = [[] for _ in range(n)]
        
        # Build tree (parent -> (child, char_bit))
        for i in range(1, n):
            bit = 1 << (ord(s[i]) - ord('a'))
            adj[parent[i]].append((i, bit))
        
        # DFS to calculate mask from root to every node
        masks = [0] * n
        stack = [(0, 0)]  # (node, current_mask)
        
        while stack:
            u, cur_mask = stack.pop()
            masks[u] = cur_mask
            for v, bit in adj[u]:
                stack.append((v, cur_mask ^ bit))
        
        # Count pairs
        ans = 0
        freq = defaultdict(int)
        
        for mask in masks:
            # Case 1: All character counts are even
            ans += freq[mask]
            
            # Case 2: Exactly one character count is odd
            for k in range(26):
                ans += freq[mask ^ (1 << k)]
            
            freq[mask] += 1
            
        return ans