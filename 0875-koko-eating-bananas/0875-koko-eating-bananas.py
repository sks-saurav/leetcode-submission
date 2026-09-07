class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def can_eat(k):
            time = 0
            for banana in piles:
                time += ((banana + k -1) // k)

            return time <= h


        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2

            if can_eat(mid):
                r = mid
            else:
                l = mid+1

        return l
