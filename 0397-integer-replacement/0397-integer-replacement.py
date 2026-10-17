# class Solution:
#     def integerReplacement(self, n: int) -> int:
#         @cache
#         def helper(x):
#             if x == 1:
#                 return 0

#             if x%2 == 0:
#                 return helper(x//2) + 1

#             else:
#                 return 1 + min(helper(x-1), helper(x+1))

            
#         return helper(n)


# class Solution:
#     def integerReplacement(self, n: int) -> int:
#         operations = 0
        
#         while n > 1:
#             if n % 2 == 0:
#                 n //= 2
#             elif n == 3 or n % 4 == 1:
#                 n -= 1
#             else:  # n % 4 == 3 and n != 3
#                 n += 1
#             operations += 1
            
#         return operations

##  BFS
class Solution:
    def integerReplacement(self, n: int) -> int:
        que = deque([(n, 0)])

        while que:
            curr, step = que.popleft()
            if curr == 1:
                return step

            if curr % 2 == 0:
                que.append((curr//2, step+1))
            else:
                que.append((curr+1, step+1))
                que.append((curr-1, step+1))

        return -1


