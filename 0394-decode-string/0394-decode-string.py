class Solution:
    def decodeString(self, s: str) -> str:
        matching_p = {}
        st = []
        for i in range(len(s)):
            if s[i] == '[': st.append(i)
            elif s[i] == ']':
                matching_p[st.pop()] = i

        def helper_dec(st, end):
            ans = ""
            i = st
            while i <= end:
                mul = 0
                # num
                while i <= end and s[i].isdigit():
                    mul = mul * 10 + int(s[i])
                    i += 1

                mul = max(mul, 1)
                # chr
                tstr = ""
                if s[i] == '[':
                    p_end = matching_p[i]
                    tstr = helper_dec(i+1, p_end-1)
                    i = p_end + 1
                else:
                    while i <= end and s[i].isalpha():
                        tstr += s[i]
                        i += 1
                ans += (mul*tstr)

            return ans

        return helper_dec(0, len(s)-1) 
