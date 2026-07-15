class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        ans = []

        def find_abv(idx, res, last_abv):
            if idx >= len(word):
                ans.append(res)
                return

            find_abv(idx+1, res+word[idx], False)

            if not last_abv:
                for j in range(idx+1, len(word)+1):
                    find_abv(j, res+str(j-idx), True)

        find_abv(0, "", False)
        return ans

