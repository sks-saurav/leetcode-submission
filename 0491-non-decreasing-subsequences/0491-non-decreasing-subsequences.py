class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        final_res = []
        found_res = set()

        def back_track(idx, res):
            if idx == len(nums):
                if len(res) > 1:
                    res_t = tuple(res)
                    if res_t not in found_res:
                        found_res.add(res_t)
                        final_res.append(list(res))
                return


            back_track(idx+1, res)

            if len(res) == 0 or nums[idx] >= res[-1]:
                res.append(nums[idx])
                back_track(idx+1, res)
                res.pop()


        back_track(0, [])
        return final_res