class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        ans = []

        def find_abv(idx, arr, last_abv):
            if idx >= len(word):
                ans.append(''.join(arr))
                return

            arr.append(word[idx])
            find_abv(idx+1, arr, False)
            arr.pop()

            if not last_abv:
                for j in range(idx+1, len(word)+1):
                    arr.append(str(j-idx))
                    find_abv(j, arr, True)
                    arr.pop()

        find_abv(0, [], False)
        return ans

