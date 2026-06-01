class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = int(1e9) + 7
        
        # If the string starts with '0', it's immediately invalid
        if not s or s[0] == '0':
            return 0
            
        # Base cases for our DP
        # prev2 represents dp[i-2] (empty string prefix)
        prev2 = 1 
        
        # prev1 represents dp[i-1] (first character prefix)
        prev1 = 9 if s[0] == '*' else 1
        
        for i in range(1, len(s)):
            curr = 0
            char = s[i]
            prev_char = s[i-1]
            
            # ----------------------------------------------------
            # 1-digit decoding (depends on prev1)
            # ----------------------------------------------------
            if char == '*':
                curr = (curr + 9 * prev1) % MOD
            elif char != '0':
                curr = (curr + prev1) % MOD
                
            # ----------------------------------------------------
            # 2-digit decoding (depends on prev2)
            # ----------------------------------------------------
            if prev_char == '*':
                if char == '*':
                    # "**" -> "11"-"19" (9 ways) + "21"-"26" (6 ways) = 15 ways
                    curr = (curr + 15 * prev2) % MOD
                elif char <= '6':
                    # "*0"-"*6" -> '*' can be '1' or '2' -> 2 ways
                    curr = (curr + 2 * prev2) % MOD
                else:
                    # "*7"-"*9" -> '*' can only be '1' -> 1 way
                    curr = (curr + prev2) % MOD
                    
            elif prev_char == '1':
                if char == '*':
                    # "1*" -> "11"-"19" -> 9 ways
                    curr = (curr + 9 * prev2) % MOD
                else:
                    # "10"-"19" -> 1 way
                    curr = (curr + prev2) % MOD
                    
            elif prev_char == '2':
                if char == '*':
                    # "2*" -> "21"-"26" -> 6 ways
                    curr = (curr + 6 * prev2) % MOD
                elif char <= '6':
                    # "20"-"26" -> 1 way
                    curr = (curr + prev2) % MOD
                    
            # ----------------------------------------------------
            # Shift states forward for the next iteration
            # ----------------------------------------------------
            prev2 = prev1
            prev1 = curr
            
        return prev1