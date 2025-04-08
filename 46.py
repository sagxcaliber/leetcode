from typing import *

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        idx = 0
        perm = [0] * len(nums)
        uni = [False] * len(nums)
        final_ans = []

        def backTrack(nums, uni, idx, perm):

            if len(nums) == idx:
                final_ans.append(perm[:])
                return

            for x in range(len(nums)):
                if not uni[x] :
                    uni[x] = True
                    perm[idx] = nums[x]
                    backTrack(nums, uni, idx + 1, perm)
                    uni[x] = False
                    perm[idx] = 0

        backTrack(nums, uni, idx, perm)
        return final_ans


s=Solution()
res=s.permute([1,2,3])
print(res)