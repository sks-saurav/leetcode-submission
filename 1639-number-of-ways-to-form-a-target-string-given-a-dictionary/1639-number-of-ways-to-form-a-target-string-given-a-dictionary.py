class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = int(1e9) + 7
        m = len(words[0])
        n = len(target)
        
        freq = [Counter() for _ in range(m)]
        for word in words:
            for i, char in enumerate(word):
                freq[i][char] += 1

        @cache
        def helper(wi, ti):
            if ti >= n:
                return 1
            if wi >= m:
                return 0

            ways = helper(wi + 1, ti)

            char_needed = target[ti]
            if freq[wi][char_needed] > 0:
                ways += freq[wi][char_needed] * helper(wi + 1, ti + 1)
                ways %= MOD

            return ways

        return helper(0, 0)