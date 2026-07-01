
# PREMIUM
class BIT:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def add(self, i, delta):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

class Solution:
    def subarraysWithMoreOnesThanZeroes(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Size needs to accommodate sums from -n to n.
        # Shift everything by n + 2 so the minimum possible sum (-n) maps to 2.
        # Max sum (n) maps to 2n + 2. Tree array size = 2n + 3.
        bit = BIT(2 * n + 3)
        offset = n + 2
        
        # Base case: a prefix sum of 0 before any elements are processed
        bit.add(0 + offset, 1)
        
        current_prefix = 0
        result = 0
        
        for num in nums:
            # Step 1: Update running prefix sum (treat 0 as -1)
            current_prefix += 1 if num == 1 else -1
            
            # Step 2: Query BIT for strictly smaller prefix sums
            # We want elements < current_prefix, so we query (current_prefix + offset - 1)
            result += bit.query(current_prefix + offset - 1)
            result %= MOD
            
            # Step 3: Add current prefix sum to the BIT
            bit.add(current_prefix + offset, 1)
            
        return result


