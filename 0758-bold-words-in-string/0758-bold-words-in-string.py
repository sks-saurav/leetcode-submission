class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        arr = []
        for word in words:
            index = s.find(word)
            while index != -1:
                arr.append([index, index+len(word)-1])
                index = s.find(word, index + 1)


        arr.sort()
        merged_arr = []
        if len(arr) != 0:
            merged_arr.append(arr[0])
            for i in range(1, len(arr)):
                if merged_arr[-1][1] + 1 >= arr[i][0]:
                    merged_arr[-1][1] = max(merged_arr[-1][1], arr[i][1])
                else:
                    merged_arr.append(arr[i])

        st, end = set(), set()
        for a in merged_arr:
            st.add(a[0])
            end.add(a[1]+1)
        
        ans = []
        for i in range(len(s)):
            if i in st:
                ans.append('<b>')
            elif i in end:
                ans.append('</b>')
            ans.append(s[i])

        if len(s) in end:
            ans.append('</b>')
            

        return ''.join(ans)
