import math
from functools import cache

class Solution:
    def soupServings(self, n: int) -> float:
        # If n is large enough, the probability of A emptying first approaches 1
        if n > 4800:
            return 1.0
        
        # Scale down by 25
        n = math.ceil(n / 25)
        
        @cache
        def soup_dp(a: int, b: int) -> float:
            # Base cases: return the final probability directly
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            
            # Recursive step
            prob = 0.0
            for da, db in [(4, 0), (3, 1), (2, 2), (1, 3)]:
                prob += 0.25 * soup_dp(a - da, b - db)
                
            return prob
        
        return soup_dp(n, n)