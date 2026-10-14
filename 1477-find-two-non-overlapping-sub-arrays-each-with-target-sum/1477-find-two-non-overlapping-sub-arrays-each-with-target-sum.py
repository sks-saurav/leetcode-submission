class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        MAX = float('inf')
        minLenTill = [MAX] * n
        currMinLen = MAX
        prevSum = {0:-1}
        currSum = 0
        ans = MAX

        for i in range(n):
            currSum += arr[i]
            val = currSum - target
            if val in prevSum:
                j = prevSum[val]
                currLen = i-j
                if j >= 0 and minLenTill[j] != MAX:
                    ans = min(ans, currLen + minLenTill[j])

                currMinLen = min(currMinLen, currLen)
            minLenTill[i] = currMinLen

            prevSum[currSum] = i

        return ans if ans != MAX else -1
