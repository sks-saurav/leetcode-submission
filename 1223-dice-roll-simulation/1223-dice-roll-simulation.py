class Solution:
    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        MOD = 10**9 + 7
        
        # dp[j][k] represents the number of valid sequences ending with 
        # face j (0-indexed) exactly k consecutive times.
        # k goes up to 15 because the max value in rollMax is 15.
        dp = [[0] * 16 for _ in range(6)]
        
        # Base case: for a sequence of length 1, each face can appear exactly once
        for j in range(6):
            dp[j][1] = 1
            
        # Build sequences from length 2 up to n
        for _ in range(2, n + 1):
            new_dp = [[0] * 16 for _ in range(6)]
            
            # sum_dp[j] stores the total sequences ending in face j from the previous roll
            sum_dp = [sum(row) % MOD for row in dp]
            total_sum = sum(sum_dp) % MOD
            
            for j in range(6):
                # 1. Start a new sequence of face j by appending j to any sequence
                # that did NOT end in j on the previous roll.
                new_dp[j][1] = (total_sum - sum_dp[j]) % MOD
                
                # 2. Continue an existing sequence of face j.
                for k in range(2, rollMax[j] + 1):
                    new_dp[j][k] = dp[j][k - 1]
                    
            dp = new_dp
            
        # Sum up all valid combinations of length n
        return sum(sum(row) % MOD for row in dp) % MOD