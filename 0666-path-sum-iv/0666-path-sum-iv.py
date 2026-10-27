class Solution:
    def pathSum(self, nums: List[int]) -> int:
        tree = {}
        for n in nums:
            d = n // 100
            p = (n // 10) % 10
            v = n % 10
            tree[(d, p)] = v

        total_sum = 0

        def dfs(d: int, p: int, current_sum: int):
            nonlocal total_sum
            current_sum += tree[(d, p)]

            left = (d + 1, 2 * p - 1)
            right = (d + 1, 2 * p)

            is_leaf = True
            if left in tree:
                is_leaf = False
                dfs(left[0], left[1], current_sum)
            if right in tree:
                is_leaf = False
                dfs(right[0], right[1], current_sum)

            if is_leaf:
                total_sum += current_sum

        if nums:
            dfs(1, 1, 0)

        return total_sum