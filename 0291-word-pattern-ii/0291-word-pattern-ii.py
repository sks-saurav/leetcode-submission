# PREMIUM

class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        bmap = {}
        visited = set()

        def matchPattern(pi, si):
            if pi == len(pattern) and si == len(s): return True
            if pi == len(pattern) or si == len(s):  return False

            key = pattern[pi]
                
            if key in bmap:
                mapped_str = bmap[key]
                if mapped_str != s[si: si+len(mapped_str)]:
                    return False
                return matchPattern(pi+1, si+len(mapped_str))

            for sj in range(si+1, len(s)+1):
                nxt_str =  s[si:sj]
                if nxt_str in visited:
                    continue
                bmap[key] = nxt_str
                visited.add(nxt_str)
                if matchPattern(pi+1, sj):
                    return True
                del bmap[key]
                visited.remove(nxt_str)

            return False

        return matchPattern(0, 0)


            
