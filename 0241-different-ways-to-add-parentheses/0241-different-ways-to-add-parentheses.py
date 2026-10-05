# Iterative
import re

class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        # 1. Parse into numbers and operators
        nums = [int(x) for x in re.split(r'[+\-*]', expression)]
        ops = re.findall(r'[+\-*]', expression)
        
        n = len(nums)
        if n == 1:
            return nums

        # 2. dp[i][j] stores all evaluation results for nums[i...j]
        dp = [[[] for _ in range(n)] for _ in range(n)]

        # 3. Base cases: interval of length 1 (single numbers)
        for i in range(n):
            dp[i][i] = [nums[i]]

        # 4. Fill DP table by increasing interval length
        for length in range(2, n + 1):          # length of interval
            for i in range(n - length + 1):      # start index
                j = i + length - 1               # end index
                
                # Split at operator k (between nums[k] and nums[k+1])
                for k in range(i, j):
                    op = ops[k]
                    left_results = dp[i][k]
                    right_results = dp[k + 1][j]
                    
                    for a in left_results:
                        for b in right_results:
                            if op == '+':
                                dp[i][j].append(a + b)
                            elif op == '-':
                                dp[i][j].append(a - b)
                            elif op == '*':
                                dp[i][j].append(a * b)

        return dp[0][n - 1]

# MEMO
# class Solution:
#     def diffWaysToCompute(self, expression: str) -> list[int]:
        
#         @lru_cache(maxsize=None)
#         def compute(exp: str) -> list[int]:
#             # Base case: if expression is just a number
#             if exp.isdigit():
#                 return [int(exp)]
            
#             results = []
#             for i, ch in enumerate(exp):
#                 if ch in "+-*":
#                     # Divide: compute all values for left and right expressions
#                     left_results = compute(exp[:i])
#                     right_results = compute(exp[i+1:])
                    
#                     # Conquer: combine every pair of results
#                     for a in left_results:
#                         for b in right_results:
#                             if ch == '+':
#                                 results.append(a + b)
#                             elif ch == '-':
#                                 results.append(a - b)
#                             elif ch == '*':
#                                 results.append(a * b)
                                
#             return results

#         return compute(expression)