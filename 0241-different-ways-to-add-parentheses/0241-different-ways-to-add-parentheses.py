from functools import lru_cache

class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        
        @lru_cache(maxsize=None)
        def compute(exp: str) -> list[int]:
            # Base case: if expression is just a number
            if exp.isdigit():
                return [int(exp)]
            
            results = []
            for i, ch in enumerate(exp):
                if ch in "+-*":
                    # Divide: compute all values for left and right expressions
                    left_results = compute(exp[:i])
                    right_results = compute(exp[i+1:])
                    
                    # Conquer: combine every pair of results
                    for a in left_results:
                        for b in right_results:
                            if ch == '+':
                                results.append(a + b)
                            elif ch == '-':
                                results.append(a - b)
                            elif ch == '*':
                                results.append(a * b)
                                
            return results

        return compute(expression)