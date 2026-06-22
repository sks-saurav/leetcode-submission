class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)

        ans = float('inf')

        for ch in 'balloon':
            if ch == 'l' or ch == 'o':
                ans = min(ans, count[ch]//2)
            else:
                ans = min(ans, count[ch])

        return 0 if ans == float('inf') else ans