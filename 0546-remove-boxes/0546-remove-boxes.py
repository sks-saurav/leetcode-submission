class Solution:
    def removeBoxes(self, boxes):
        n = len(boxes)
        if not n:
            return 0
        
        # dp[l][r][k]
        dp = [[[0] * n for _ in range(n)] for _ in range(n)]
        
        # Iterate over the length of the subarray
        for length in range(1, n + 1):
            # Iterate over the start index of the subarray
            for l in range(n - length + 1):
                r = l + length - 1
                
                # k is the number of boxes to the right of 'r' with the same color as boxes[r].
                # The maximum possible k is bounded by the number of elements to the right of r.
                for k in range(n - r):
                    
                    # Option 1: Remove boxes[r] along with the k matching boxes to its right
                    res = (k + 1) ** 2
                    if l < r:
                        res += dp[l][r - 1][0]
                    
                    # Option 2: Find a matching box inside the current subarray to merge with
                    for i in range(l, r):
                        if boxes[i] == boxes[r]:
                            # dp[i + 1][r - 1][0] handles the boxes between i and r
                            # dp[l][i][k + 1] handles the left part, now with k+1 matching boxes to its right
                            res = max(res, dp[l][i][k + 1] + dp[i + 1][r - 1][0])
                            
                    dp[l][r][k] = res
                    
        return dp[0][n - 1][0]


# # Solution exp: https://www.youtube.com/watch?v=_8hSyaxVRZ8
# class Solution:
#     def removeBoxes(self, boxes: List[int]) -> int:
#         dp = {}

#         def helper(l, r, count):
#             if l > r: return 0

#             state = (l,r,count)
#             if state in dp: return dp[state]

#             while l+1 <= r and boxes[l] == boxes[l+1]:
#                 count += 1
#                 l += 1
#             # saurav: first box is missed to count in above while loop so (count+1)
#             ans = (count+1)*(count+1) + helper(l+1, r, 0)

#             for m in range(l+1, r+1):
#                 if boxes[m] == boxes[l]:
#                     tans = helper(m, r, count+1) + helper(l+1, m-1, 0)
#                     ans = max(ans, tans)

#             dp[state] = ans
#             return ans

#         return helper(0, len(boxes)-1, 0)
