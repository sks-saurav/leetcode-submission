class Solution:
    def processStr(self, s: str) -> str:
        st = []

        for ch in s:
            if ch == '*':
                if st:
                    st.pop()

            elif ch == '#':
                l = len(st)
                for i in range(l):
                    st.append(st[i])

            elif ch == '%':
                tst = []
                while st:
                    tst.append(st.pop())
                st = tst

            else:
                st.append(ch)


        return ''.join(st)

