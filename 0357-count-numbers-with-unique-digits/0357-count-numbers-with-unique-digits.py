class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        @cache
        def digit_dp(s, idx, limited, lz, mask):
            if idx == len(s):
                return 1

            res = 0
            lb = 0
            ub = (ord(s[idx]) - ord('0')) if limited else 9

            for dig in range(lb, ub+1):
                n_limited = limited and dig == int(s[idx])

                if dig == 0 and lz:
                    res += digit_dp(s, idx+1, n_limited, lz, mask)
                else:
                    if (mask & (1 << dig)) == 0:
                        n_mask = mask | (1 << dig)
                        n_lz = False
                        res += digit_dp(s, idx+1, n_limited, n_lz, n_mask)

            return res

        n = 10**n - 1
        return digit_dp(str(n), 0, True, True, 0)

