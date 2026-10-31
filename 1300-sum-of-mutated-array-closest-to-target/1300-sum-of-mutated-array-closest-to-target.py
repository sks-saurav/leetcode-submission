class Solution:
    def findBestValue(self, arr: list[int], target: int) -> int:
        n = len(arr)
        psum = [0] * (n+1)
        arr.sort()
        ansVal = -1
        diff = float('inf')

        for i in range(n):
            psum[i+1] = psum[i] + arr[i]

        for val in range(0, arr[-1]+1):
            idx = bisect_right(arr, val)
            lsum = psum[idx]
            rsum = (n-idx) * val
            currSum = lsum + rsum
            currDiff = abs(currSum - target)
            
            if currDiff < diff:
                diff = currDiff
                ansVal = val

        return ansVal

            

        