class Solution:
    def findBestValue(self, arr: list[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]
            
        def get_sum(val: int) -> int:
            idx = bisect_right(arr, val)
            return prefix[idx] + (n - idx) * val

        low, high = 0, arr[-1]
        best_val = high
        
        while low <= high:
            mid = (low + high) // 2
            if get_sum(mid) >= target:
                best_val = mid
                high = mid - 1
            else:
                low = mid + 1
                
        # The optimal answer must be either best_val or best_val - 1
        sum1 = get_sum(best_val - 1)
        sum2 = get_sum(best_val)
        
        # Tie-breaker: choose smaller value if differences are equal
        if abs(target - sum1) <= abs(target - sum2):
            return best_val - 1
        return best_val