class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        maskMap = {0:-1}
        mask = 0
        vowels = {'a' : 0, 'e': 1, 'i': 2, 'o' : 3, 'u': 4}
        count = [0] * 5
        ans = 0

        for i, c in enumerate(s):
            if c in vowels:
                idx = vowels[c]
                count[idx] += 1
                if count[idx]%2 == 1:
                    mask = mask | (1 << idx)
                else:
                    mask = mask & (~(1<<idx))

            if mask in maskMap:
                pi = maskMap[mask]
                ans = max(ans, i-pi)
            else:
                maskMap[mask] = i

        return ans





        

