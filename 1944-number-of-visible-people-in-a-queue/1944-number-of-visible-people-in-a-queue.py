class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        ans = []
        n = len(heights)
        stack = []
        for i in range(n-1, -1, -1):
            person =  0
            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()
                person += 1

            if stack:
                person += 1

            ans.append(person)
            stack.append(i)

        ans.reverse()
        return ans