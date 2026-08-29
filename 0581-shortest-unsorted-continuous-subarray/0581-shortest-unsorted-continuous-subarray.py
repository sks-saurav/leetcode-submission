'''
[0,1,2,3,4,5,6,7] <- idx
[2,6,4,8,10,9,15]
[2,4,6,8,9,10,15]

 0,2,1,3,5,4,6


'''

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            stack.append(i)

        pvs = -1
        idx1 = 0
        while idx1 < len(stack):
            if stack[idx1] == pvs+1:
                pvs += 1
            else:
                break   
            idx1 += 1
        
        if idx1 == n:
            return 0

        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            stack.append(i)

        pvs = n
        idx2 = 0
        while idx2 < len(stack):
            if stack[idx2] == pvs-1:
                pvs -= 1
            else:
                break   
            idx2 += 1

        return n-idx1-idx2

        