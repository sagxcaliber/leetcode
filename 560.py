from typing import *


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        hash_map = {0: 1}
        prev_val = 0
        for x in range(len(nums)):
            prev_val = nums[x] + prev_val

            if (prev_val - k) in hash_map:
                res += hash_map[(prev_val - k)]

            if prev_val in hash_map:
                hash_map[prev_val] += 1

            else:
                hash_map[prev_val] = 1

        return res

s=Solution()
res=s.subarraySum([1,-1,0],0)
print(res)


