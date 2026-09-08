class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        arr = []
        for dig in num:
            while k > 0 and len(arr) != 0 and arr[-1] > dig:
                arr.pop()
                k -= 1
            arr.append(dig)
            
        i = 0
        while i < len(arr) and arr[i] == '0':
            i += 1

        j = len(arr)-k
        ans = "".join(arr[i:j])
        return ans if len(ans) != 0 else "0"