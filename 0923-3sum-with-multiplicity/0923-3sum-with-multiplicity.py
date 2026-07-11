class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        counter = defaultdict(int)
        MOD = int(1e9) + 7
        ans = 0
        n = len(arr)

        for i in range(n):
            for j in range(i+1, n):
                req = target - arr[i] - arr[j]
                ans = (ans + counter[req]) % MOD
            counter[arr[i]] += 1

        return ans
