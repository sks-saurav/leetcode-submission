class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        # DP
        # pairs.sort(key = lambda p : (p[0], p[1]))
        # n = len(pairs)
        # dp = [1] * n

        # for i in range(1, n):
        #     for j in range(i):
        #         if pairs[j][1] < pairs[i][0]:
        #             dp[i] = max(dp[i], dp[j]+1)

        # return max(dp)


       
        # GREEDY 
        pairs.sort(key=lambda x: x[1])
        curr_end = float('-inf')
        chain_len = 0
        
        for pair in pairs:
            # If the current pair starts after the previous pair ends
            if pair[0] > curr_end:
                chain_len += 1
                curr_end = pair[1] # Update the end of the chain
                
        return chain_len