'''
# 1
If k = 0, every subarray is distant. Otherwise, for a current prefix sum s and an earlier prefix sum p, the subarray is distant when p <= s - goal - k or p >= s - goal + k.

# 2
Compress the prefix sums and process them from left to right. Use a Fenwick tree to count earlier prefix sums in these two ranges, querying before inserting the current prefix sum.
'''
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
    def distantSubarrays(self, nums: list[int], goal: int, k: int) -> int:
        n = len(nums)
        # If k is 0, every subarray meets the condition
        if k == 0:
            return (n * (n + 1)) // 2
        
        # 1. Build prefix sums, starting with 0 for subarrays starting at index 0
        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)

        # 2. Coordinate compression: get all unique prefix sums and sort them
        unique_prefixes = sorted(list(set(prefix_sums)))
        ftree = Fenwick(len(unique_prefixes))

        ans = 0
        
        # 3. Iterate through prefix sums
        for i, s in enumerate(prefix_sums):
            # For i == 0, there are no earlier prefix sums to query, so we skip directly to insertion
            if i > 0:
                v1 = s - goal - k
                v2 = s - goal + k

                # Query 1: count of earlier prefix sums <= v1
                # bisect_right gives the number of unique prefixes <= v1, which acts as our 1-based Fenwick index
                idx1 = bisect.bisect_right(unique_prefixes, v1)
                count1 = ftree.query(idx1)

                # Query 2: count of earlier prefix sums >= v2
                # bisect_left gives the number of unique prefixes strictly < v2. 
                # If we subtract this from the total inserted so far (i), we get the count of >= v2
                # IMP (count2 = i - ftree.query(idx2))
                # Total Seen = (Count of p < v_2) + (Count of p >= v_2)
                # Substituting our variables: i = ftree.query(idx2) + count2
                # Rearranging to solve for count2: count2 = i - ftree.query(idx2)
                idx2 = bisect.bisect_left(unique_prefixes, v2)
                count2 = i - ftree.query(idx2)

                ans += count1 + count2

            # Insert current prefix sum `s` into the Fenwick tree
            # bisect_left + 1 gives us the exact 1-based rank of `s` in our unique_prefixes list
            rank = bisect.bisect_left(unique_prefixes, s) + 1
            ftree.update(rank, 1)

        return ans