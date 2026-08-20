# PREMIUM

# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
#class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        """
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#        """
# 
#    def getHeight(self, fontSize):
#        """
#        :type fontSize: int
#        :rtype int
#        """
class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo : 'FontInfo') -> int:
        def can_fit(fontsize):
            f_ht = fontInfo.getHeight(fontsize)
            if f_ht > h:
                return False

            total_w = 0
            for ch in text:
                total_w += fontInfo.getWidth(fontsize, ch)
                if total_w > w:
                    return False

            return True

        if not can_fit(fonts[0]):
            return -1

        l, r = 0, len(fonts)-1
        ans = 0
        while l < r:
            mid = (l+r+1)//2
            if can_fit(fonts[mid]):
                l = mid
            else:
                r = mid-1

        return fonts[l]