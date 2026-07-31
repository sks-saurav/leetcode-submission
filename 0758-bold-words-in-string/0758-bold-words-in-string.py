class Solution:
    def boldWords(self, words: list[str], s: str) -> str:
        n = len(s)
        bold = [False] * n
        
        # Step 1: Mark all characters that are part of any keyword as True
        for word in words:
            start = s.find(word)
            while start != -1:
                for i in range(start, start + len(word)):
                    bold[i] = True
                start = s.find(word, start + 1)
                
        ans = []
        for i in range(n):
            # If current char is bold AND (it's the first char OR previous char was not bold)
            # This means we just entered a bold section.
            if bold[i] and (i == 0 or not bold[i - 1]):
                ans.append('<b>')
                
            ans.append(s[i])
            
            # If current char is bold AND (it's the last char OR next char is not bold)
            # This means we just finished a bold section.
            if bold[i] and (i == n - 1 or not bold[i + 1]):
                ans.append('</b>')
                
        return ''.join(ans)