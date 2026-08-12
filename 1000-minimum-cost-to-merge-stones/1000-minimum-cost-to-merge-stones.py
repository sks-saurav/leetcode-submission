class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1
            
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]
            
        def range_sum(i: int, j: int) -> int:
            return prefix[j + 1] - prefix[i]
            
        memo = {}
        
        def solve(i: int, j: int) -> int:
            if i == j:
                return 0
                
            if (i, j) in memo:
                return memo[(i, j)]
                
            min_cost = float('inf')
            
            # We step by (k - 1) to ensure the left part stones[i...mid] 
            for mid in range(i, j, k - 1):
                cost = solve(i, mid) + solve(mid + 1, j)
                if cost < min_cost:
                    min_cost = cost
                    
            # If the entire subarray stones[i...j] is ready to be merged 
            # into exactly 1 pile, add the cost of this final merge.
            if (j - i) % (k - 1) == 0:
                min_cost += range_sum(i, j)
                
            memo[(i, j)] = min_cost
            return min_cost
            
        return solve(0, n - 1)



        '''
        The first thing we need to check can we merge all these piles into 1 pile ?
        we can check this : if((n-1)%(k-1) == 0) then only we can do merging.

        let's see how we can arrive at this formula

        if there are n piles given and k piles are to be merged. Then,
        After the first merge : the length of the array will be n - (k-1).
        After the second merge : the length of the array will be n - (k-1) - (k-1).
        After the third merge : the length of the array will be n - (k-1) - (k-1) - (k-1)
        and so on...

        For eg:
        [0 1 2 3 4] -> indexing
        [3,5,1,2,6] -> array elements
        length is 5

        if we do single merge of [5, 1, 2] => [8]

        [0,1,2] -> indexing
        [3,8,6] -> array elements
        length is 3 : which n - (k-1) = 5 - (k-1) = 5 - (3-1) = 5 - 2 = 3;

        So, we know that after m merges the length must be 1, if we can merge piles
        So, we can say that Cost for single merge is k-1 and for m merges will be m*(k-1);

        total_merges = m * (k-1);

        Given in the question : A move consists of merging exactly k consecutive piles
        into one pile and in the end only single pile is left.,

        So, we can say that:
        N - total_merges = 1
        N - m*(k-1) = 1;
        N - 1 = m*(k-1);
        m = (N-1) / (k-1)

        now, "m" must be positive number then only we can merge them
        '''