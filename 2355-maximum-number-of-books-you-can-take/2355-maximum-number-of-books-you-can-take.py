# PREMIUM
class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        nums = [books[i]-i for i in range(len(books))]
        stack = [-1]
        taken = [0]
        ans = 0

        for i in range(len(books)):
            while len(stack) > 1 and nums[stack[-1]] >= nums[i]:
                stack.pop()
                taken.pop()
            
            count = 0
            n = min(books[i], i-stack[-1])
            last = books[i]
            first = last - (n-1)
            count = (n * (first + last)) // 2
            count += taken[-1]

            stack.append(i)
            taken.append(count)
            ans = max(ans, count)
        return ans
        