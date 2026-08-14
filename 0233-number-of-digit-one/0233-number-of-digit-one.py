class Solution:
    def countDigitOne(self, n: int) -> int:
        
        def digit_dp(s, idx, is_limited, one_count):
            if idx == len(s):
                return one_count

            state = (idx, is_limited, one_count)
            if state in dp:
                return dp[state]

            lb = 0
            ub = (ord(s[idx])-ord('0')) if is_limited else 9
            res = 0

            for dig in range(lb, ub+1):
                next_is_limited = is_limited and dig == int(s[idx])
                next_one_count = one_count + 1 if dig == 1 else one_count
                
                res += digit_dp(s, idx+1, next_is_limited, next_one_count)

            dp[state] = res
            return res

        dp = {}
        return digit_dp(str(n), 0, True, 0)