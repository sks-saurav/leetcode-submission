class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # stores pairs: (prev_string, repeat_count)
        curr_str = ""
        curr_num = 0

        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            elif ch == '[':
                # Save the context of the parent level
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            elif ch == ']':
                # Pop context and resolve the repeated block
                prev_str, repeat_k = stack.pop()
                curr_str = prev_str + curr_str * repeat_k
            else:
                # Regular character
                curr_str += ch

        return curr_str

# class Solution:
#     def decodeString(self, s: str) -> str:
#         matching_p = {}
#         st = []
#         for i in range(len(s)):
#             if s[i] == '[': st.append(i)
#             elif s[i] == ']':
#                 matching_p[st.pop()] = i

#         def helper_dec(st, end):
#             ans = ""
#             i = st
#             while i <= end:
#                 mul = 0
#                 # num
#                 while i <= end and s[i].isdigit():
#                     mul = mul * 10 + int(s[i])
#                     i += 1

#                 mul = max(mul, 1)
#                 # chr
#                 tstr = ""
#                 if s[i] == '[':
#                     p_end = matching_p[i]
#                     tstr = helper_dec(i+1, p_end-1)
#                     i = p_end + 1
#                 else:
#                     ta, tb = i, i
#                     while i <= end and s[i].isalpha():
#                         tb += 1
#                         i += 1
#                     tstr = s[ta:tb]
#                 ans += (mul*tstr)
#             return ans

#         return helper_dec(0, len(s)-1) 
