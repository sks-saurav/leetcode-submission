class Solution:
    def mat_mul(self ,A ,B ,mod):
        n = len(A)
        C = [[0] * n for _ in range(n)]
        for i in range(n):
            for k in range(n):
                if A[i][k] == 0:
                    continue
                for j in range(n):
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
        return C


    def mat_pow(self, A, p , mod):
        n = len(A)
        res = [[int(i == j) for j in range(n)] for i in range(n)]
        base = A
        while p > 0:
            if p & 1:
                res = self.mat_mul(res, base, mod)
            base = self.mat_mul(base, base, mod)
            p >>= 1
        return res


    def checkRecord(self, n: int) -> int:
        MOD = 1_000_000_007

        # 6x6 Transition Matrix
        T = [
            [1, 1, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
        ]

        # Compute T^n
        T_n = self.mat_pow(T, n, MOD)

        # V_n = T^n * V_0, where V_0 = [1, 0, 0, 0, 0, 0]^T
        # This means V_n is column 0 of T_n: V_n[i] = T_n[i][0]
        total_valid = sum(T_n[i][0] for i in range(6)) % MOD

        return total_valid