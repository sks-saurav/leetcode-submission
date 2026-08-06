class Solution:
    def minPartitions(self, n: str) -> int:
        ans = 0
        for ch in n:
            val = ord(ch)-ord('0')
            ans = max(ans, val)

        return ans