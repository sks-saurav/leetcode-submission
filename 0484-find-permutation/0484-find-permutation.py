# PREMIUM
'''
Start by initializing your array with the absolute smallest permutation: [1, 2, 3, ..., n].

Iterate through the string s. Whenever you find a contiguous block of 'D's, take that specific sub-section in your array and reverse it.

Eg.. s = "DI"
You need numbers 1, 2, and 3.
Step 1: Push 1.
Stack: [1]
Look at s[0]: It's 'D'. We want decreasing, so we just wait. Do nothing.

Step 2: Push 2.
Stack: [1, 2]
Look at s[1]: It's 'I'. This is the trigger!
Pop everything into the result array.
Result: [2, 1] (Notice how the 'D' relationship is now satisfied!).

Step 3: Push 3.
Stack: [3]
Look at s[2]: Out of bounds! We hit the end. This is the final trigger.
Pop everything left.
Final Result: [2, 1, 3]

'''

class Solution:
    def findPermutation(self, s: str) -> List[int]:
        n = len(s) + 1
        si = 0
        stack = []
        ans = []

        for i in range(1,n+1):
            stack.append(i)
            if si < len(s) and s[si] == 'I':
                while stack:
                    ans.append(stack.pop())
            si += 1

        while stack:
            ans.append(stack.pop())

        return ans