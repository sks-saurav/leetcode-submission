class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        i = 0
        for pe in pushed:
            while st and i < len(popped) and popped[i] == st[-1]:
                st.pop()
                i += 1

            st.append(pe)

        while st and i < len(popped) and popped[i] == st[-1]:
            st.pop()
            i += 1
            
        return len(st) == 0