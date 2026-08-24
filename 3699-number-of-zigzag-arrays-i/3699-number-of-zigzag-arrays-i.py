class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        
        # dp0[v] = number of valid sequences ending at value v, where the NEXT step must INCREASE
        # dp1[v] = number of valid sequences ending at value v, where the NEXT step must DECREASE
        dp0 = [1] * m
        dp1 = [1] * m
        
        for _ in range(2, n + 1):
            new_dp0 = [0] * m
            new_dp1 = [0] * m
            
            # 1. Populate new_dp0 (next step increases, meaning current step DECREASED)
            # This requires taking the sum of dp1[u] for all u > v (Suffix Sum)
            running_sum = 0
            for v in range(m - 1, -1, -1):
                new_dp0[v] = running_sum
                running_sum = (running_sum + dp1[v]) % MOD
                
            # 2. Populate new_dp1 (next step decreases, meaning current step INCREASED)
            # This requires taking the sum of dp0[u] for all u < v (Prefix Sum)
            running_sum = 0
            for v in range(m):
                new_dp1[v] = running_sum
                running_sum = (running_sum + dp0[v]) % MOD
                
            dp0 = new_dp0
            dp1 = new_dp1
            
        # The total valid ZigZag arrays is the sum of all valid sequences ending in any value 
        # going in either direction.
        ans = (sum(dp0) + sum(dp1)) % MOD
        return ans

'''
The Math Behind the Optimization
Let's look at your original loop for an increasing sequence (inc == 1):
helper(idx, pvs, 1) = helper(idx+1, pvs+1, 0) + helper(idx+1, pvs+2, 0) + ... + helper(idx+1, r, 0)

If we look at the state exactly one step higher (pvs + 1), it expands to:
helper(idx, pvs+1, 1) = helper(idx+1, pvs+2, 0) + ... + helper(idx+1, r, 0)

Notice that the second equation is entirely contained within the first one! We can substitute it to create an O(1) transition:
helper(idx, pvs, 1) = helper(idx+1, pvs+1, 0) + helper(idx, pvs+1, 1)

The same logic applies to the decreasing sequence (inc == 0):
helper(idx, pvs, 0) = helper(idx+1, pvs-1, 1) + helper(idx, pvs-1, 0)
'''

# class Solution:
#     def zigZagArrays(self, n: int, l: int, r: int) -> int:
#         sys.setrecursionlimit(5000)
#         MOD = int(1e9) + 7
#         memo = {}

#         def helper(idx, pvs, inc):
#             if idx == n:
#                 return 1
            
#             if inc == 1 and pvs >= r:
#                 return 0
#             if inc == 0 and pvs <= l:
#                 return 0
                
#             state = (idx, pvs, inc)
#             if state in memo:
#                 return memo[state]

#             if inc == 1:
#                 ans = (helper(idx + 1, pvs + 1, 0) + helper(idx, pvs + 1, 1)) % MOD
#             else:
#                 ans = (helper(idx + 1, pvs - 1, 1) + helper(idx, pvs - 1, 0)) % MOD

#             memo[state] = ans
#             return ans

#         res = 0
#         for dig in range(l, r + 1):
#             res = (res + helper(1, dig, 0)) % MOD
#             res = (res + helper(1, dig, 1)) % MOD

#         return res


# class Solution:
#     def zigZagArrays(self, n: int, l: int, r: int) -> int:
#         MOD = int(1e9) + 7

#         def helper(idx, pvs, inc):
#             nonlocal MOD
#             if idx == n:
#                 return 1
            
#             state = (idx, pvs, inc)
#             if state in memo:
#                 return memo[state]

#             ans = 0
#             if inc:
#                 for curr in range(pvs+1, r+1):
#                     ans = (ans + helper(idx+1, curr, 1-inc)) % MOD
#             else:
#                 for curr in range(pvs-1, l-1, -1):
#                     ans = (ans + helper(idx+1, curr, 1-inc))

#             memo[state] = ans
#             return ans

#         memo = {}
#         res = 0
#         for dig in range(l, r+1):
#             res = (res + helper(1, dig, 0)) % MOD
#             res = (res + helper(1, dig, 1)) % MOD

#         return res