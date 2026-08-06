class Solution:
    def minPartitions(self, n: str) -> int:
        covered = 0
        ans = 0
        for ch in n:
            val = ord(ch)-ord('0')
            diff = max(0, val-covered)
            covered += diff
            ans += diff

        return ans