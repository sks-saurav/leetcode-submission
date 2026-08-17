# class Solution:
#     def new21Game(self, n: int, k: int, maxPts: int) -> float:
        
#         def dp_21(score):
#             if score >= k:
#                 return 1.0 if score <= n else 0.0
            
#             if score in memo:
#                 return memo[score]

#             prob = 0
#             for drawn_number in range(1, maxPts+1):
#                 prob += (dp_21(score + drawn_number)) / maxPts

#             memo[score] = prob
#             return prob
        
#         memo = {}
#         return dp_21(0)

# class Solution:
#     def new21Game(self, n: int, k: int, maxPts: int) -> float:
#         dp = [0] * (n + 1)
#         dp[0] = 1
#         for i in range(1, n + 1):
#             for j in range(1, maxPts + 1):
#                 if i - j >= 0 and i - j < k:
#                     dp[i] += dp[i - j] / maxPts
#         return sum(dp[k:])

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # Edge cases: 
        # 1. k == 0: We start with 0 points and stop immediately. Since n >= 0, prob is 1.0.
        # 2. n >= k + maxPts: Even if we start from k-1 and draw the max card, we won't exceed n.
        if k == 0 or n >= k + maxPts:
            return 1.0
        
        # dp[i] represents the probability of reaching exactly i points.
        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        
        # This sliding window holds the sum of probabilities of previous states 
        # that can legally roll a die to land on the current state.
        window_sum = 1.0
        result = 0.0
        
        for i in range(1, n + 1):
            # The probability of landing on `i` is the sum of valid previous probabilities / maxPts
            dp[i] = window_sum / maxPts
            
            # If `i` is less than `k`, we can continue drawing cards from this state,
            # so we add its probability to our sliding window.
            if i < k:
                window_sum += dp[i]
            # If `i` is >= `k`, the game stops. We don't add it to the window_sum, 
            # but we DO add it to our final result (since i <= n).
            else:
                result += dp[i]
                
            # As our window slides forward, we must remove the probability of the state 
            # that just fell out of the window's reach (i.e., it's further than maxPts away).
            if i - maxPts >= 0:
                window_sum -= dp[i - maxPts]
                
        return result