class Solution:
    def minTransfers(self, transactions: list[list[int]]) -> int:
        hm = defaultdict(int)
        for transaction in transactions:
            hm[transaction[0]] -= transaction[2]
            hm[transaction[1]] += transaction[2]

        balances = []
        min_opers = float('inf')
        for val in list(hm.values()):
            if val != 0:
                balances.append(val)
        if not balances:
            return 0

        def dfs(i, opers=0):
            nonlocal min_opers
            if opers >= min_opers:
                return
            # skip people whose balances are already zero
            while i < len(balances) and balances[i] == 0:
                i += 1
            if i == len(balances):
                min_opers = min(opers, min_opers)
                return
            curr_balance = balances[i]

            for j in range(i + 1, len(balances)):
                if curr_balance * balances[j] < 0:
                    # Settle person i through person j
                    balances[j] += curr_balance
                    dfs(i + 1, opers=opers + 1)
                    # Undo the transfer
                    balances[j] -= curr_balance
                    # An exact match makes further partners unnecessary
                    if balances[j] + curr_balance == 0:
                        break

        dfs(0)
        return min_opers