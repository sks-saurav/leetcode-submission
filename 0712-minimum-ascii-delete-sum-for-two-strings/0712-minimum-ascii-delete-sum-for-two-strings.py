class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        @cache
        def helper(i1, i2):
            cost = 0
            if i1 < 0:
                for i in range(i2+1):
                    cost += ord(s2[i])
                return cost

            if i2 < 0:
                for i in range(i1+1):
                    cost += ord(s1[i])
                return cost

            cost1 = float('inf')
            
            if s1[i1] == s2[i2]:
                cost1 = helper(i1-1, i2-1)

            cost2 = helper(i1-1, i2) + ord(s1[i1])
            cost3 = helper(i1, i2-1) + ord(s2[i2])

            return min(cost1, cost2, cost3)


        return helper(len(s1)-1, len(s2)-1)

            
                