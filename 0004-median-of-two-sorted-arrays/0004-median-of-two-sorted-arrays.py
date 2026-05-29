class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def pos(arr, val):
            l, r = 0, len(arr)-1
            ans = -1

            while l <= r:
                mid = (l+r)//2
                if arr[mid] <= val:
                    ans = mid
                    l = mid+1
                else:
                    r = mid-1
            return ans+1

        def kthElement(k):
            if len(nums1) != 0 and len(nums2) != 0:
                min_ele = min(nums1[0], nums2[0])
                max_ele = max(nums1[-1], nums2[-1])
            elif len(nums1) == 0:
                min_ele = nums2[0]
                max_ele = nums2[-1]
            else:
                min_ele = nums1[0]
                max_ele = nums1[-1]

            ans = 0
            while min_ele <= max_ele:
                mid_ele = (min_ele + max_ele) // 2
                curr_pos = pos(nums1, mid_ele) + pos(nums2, mid_ele)
                if curr_pos >= k:
                    ans = mid_ele
                    max_ele = mid_ele - 1
                else:
                    min_ele = mid_ele + 1
                    
            return ans

        ####################################################################
        if len(nums1) == 0 and len(nums2) == 0:
            return 0

        total_ele = len(nums1) + len(nums2)
        mid = total_ele // 2

        if total_ele%2 == 1:
            return kthElement(mid+1)
        return (kthElement(mid) + kthElement(mid+1)) / 2
