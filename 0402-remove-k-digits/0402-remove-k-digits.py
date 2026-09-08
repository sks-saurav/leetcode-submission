class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        arr = []
        for dig in num:
            while k > 0 and len(arr) != 0 and arr[-1] > dig:
                arr.pop()
                k -= 1
            arr.append(dig)
            
        j = len(arr)-k
        ans = "".join(arr[:j])
        ans = ans.lstrip('0')
        return ans if len(ans) != 0 else "0"