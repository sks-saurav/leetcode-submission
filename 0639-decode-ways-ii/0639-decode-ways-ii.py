class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = int(1e9) + 7

        @cache
        def helper(idx):
            if idx >= len(s):
                return 1

            ways = 0
            ch = s[idx]
            
            if ch == '0':
                return 0

            if ch == '*':
                ways = (ways + (9 * helper(idx+1))) % MOD
                if idx + 1 < len(s):
                    n_ch = s[idx+1]
                    if n_ch == '*':
                        # "**" can be "11"-"19" (9) or "21"-"26" (6) -> 15 ways
                        ways = (ways + (15 * helper(idx+2))) % MOD
                    elif n_ch <= '6':
                        # "*0" to "*6" -> '*' can be '1' or '2' -> 2 ways
                        ways = (ways + (2 * helper(idx+2))) % MOD
                    else:
                        # "*7" to "*9" -> '*' can only be '1' -> 1 way
                        ways = (ways + helper(idx+2)) % MOD

            else:
                ways = (ways + helper(idx+1)) % MOD

                if idx+1 < len(s):
                    n_ch = s[idx+1]

                    if ch == '1':
                        if n_ch == '*':
                            ways = (ways + (9 * helper(idx+2))) % MOD
                        else:
                            ways = (ways + helper(idx+2)) % MOD

                    elif ch == '2':
                        if n_ch == '*':
                            ways = (ways + (6 * helper(idx+2))) % MOD
                        elif (ord(n_ch) - ord('0')) <= 6:
                            ways = (ways + helper(idx+2)) % MOD

            return ways


        return helper(0)
            
