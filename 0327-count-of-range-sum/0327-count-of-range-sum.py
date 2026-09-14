class Fenwick:
    def __init__(self, capacity):
        self.n = capacity + 1
        self.tree = [0] * self.n

    def update(self, idx, delta):
        while idx < self.n:
            self.tree[idx] += delta
            idx += (idx & -idx)

    def query(self, idx):
        s = 0
        while idx > 0:
            s += self.tree[idx]
            idx -= (idx & -idx)
        return s

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        psum = [0]
        for ele in nums:
            psum.append(psum[-1] + ele)

        unique_prefixes = sorted(list(set(psum)))
        ftree = Fenwick(len(unique_prefixes))
        ans = 0
        
        for s in psum:
            '''
            We want to find how many previous prefix sums fall in [s - upper, s - lower]
            -> lower <= RangeSum(i, j) <= upper
            -> lower <= psum[j] - psum[i] <= upper
            -> s is exactly psum[j].
            -> lower <= s - psum[i] <= upper
            -> s - upper <= psum[i] <= s - lower
            '''
            left_rank = bisect.bisect_left(unique_prefixes, s - upper)
            right_rank = bisect.bisect_right(unique_prefixes, s - lower)-1
            
            # Count elements in [left_rank, right_rank]
            ans += ftree.query(right_rank+1) - ftree.query(left_rank)
            
            rank = bisect.bisect_left(unique_prefixes, s) + 1
            ftree.update(rank, 1)
            
        return ans