# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n

#         dp_1 = 1
#         dp_2 = 2

#         for i in range(3, n+1):
#             dp = dp_1 + dp_2
#             dp_1 = dp_2
#             dp_2 = dp

#         return dp


# Matrix exponentiation
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        M = [
            [1, 1],
            [1, 0]
        ]
        op = Matrix()
        MN = op.pow(M, n)

        return MN[0][0]



class Matrix:
    def pow(self, A, n):
        if n == 0:
            return A

        dim = len(A)
        res = [[int(i==j) for j in range(dim)] for i in range(dim)]
        curr = A

        while n > 0:
            if n&1 == 1:
                res = self.multiply(res, curr)
            curr = self.multiply(curr, curr)
            n = n>>1
        
        return res

    def multiply(self, A, B):
        dim = len(A)
        res = [[0] * dim for _ in range(dim)]
        
        for i in range(dim):
            for j in range(dim):
                for k in range(dim):
                    res[i][j] += (A[i][k] * B[k][j])

        return res

        
