# PREMIUM
'''
 the problem requires that strictly fewer books are taken from shelf $i$ than shelf $i+1$ moving backwards ($books[j] - j \ge books[i] - i$ condition, or transforming the array to $nums[i] = books[i] - i$). Without this transformation, a taller shelf might violate the strict decrease condition relative to its index distance.
'''
class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)
        nums = [books[i] - i for i in range(n)]
        stack = []
        dp = [0] * n
        ans = 0

        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            
            j = stack[-1] if stack else -1
            count = min(books[i], i - j)
            
            first = books[i] - count + 1
            last = books[i]
            # sum of concecutive intger (3,4,5,6,7)
            # sum = (n*(first + last) / 2) , n = number of element 
            # sum = (5 * (3 + 7)) / 2
            s = (count * (first + last)) // 2
            
            if j != -1:
                s += dp[j]
            
            dp[i] = s
            ans = max(ans, dp[i])
            stack.append(i)
            
        return ans