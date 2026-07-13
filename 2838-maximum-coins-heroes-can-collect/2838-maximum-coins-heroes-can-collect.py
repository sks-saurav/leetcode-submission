# PREMIUM

class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        h_arr = [(heroes[i], i) for i in range(len(heroes))]
        m_arr = [(monsters[i], coins[i]) for i in range(len(coins))]
        h_arr.sort()
        m_arr.sort()

        n, m = len(heroes), len(monsters)
        i, j = 0, 0
        res = [0] * n
        curr_coin = 0
        while i < n and j < m:
            if m_arr[j][0] <= h_arr[i][0]:
                curr_coin += m_arr[j][1]
                j += 1
            else:
                curr_hero_power = h_arr[i][0]
                while i < n and h_arr[i][0] == curr_hero_power:
                    res[h_arr[i][1]] = curr_coin
                    i += 1

        while i < n:
            curr_hero_power = h_arr[i][0]
            while i < n and h_arr[i][0] == curr_hero_power:
                res[h_arr[i][1]] = curr_coin
                i += 1

        return res