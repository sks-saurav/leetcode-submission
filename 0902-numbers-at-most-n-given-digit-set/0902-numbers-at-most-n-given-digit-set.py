class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        # lz = leading zeros
        
        def digit_dp(s, idx, limited, lz):
            if idx == len(s):
                return 1

            state = (idx, limited, lz)
            if state in dp: return dp[state]

            res = 0
            lb = 0
            ub = (ord(s[idx]) - ord('0')) if limited else 9

            for dig in range(lb, ub+1):
                next_limited = limited and dig == int(s[idx])
                if dig == 0 and lz:
                    res += digit_dp(s, idx+1, next_limited, lz)
                else:
                    if dig in valid:
                        res += digit_dp(s, idx+1, next_limited, False)

            dp[state] = res
            return res


        valid = set()
        for d in digits:
            valid.add(int(d))

        dp = {}
        return digit_dp(str(n), 0, True, True)-1