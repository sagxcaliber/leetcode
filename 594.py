from typing import *


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums = sorted(nums)
        left = 0
        right = 1
        result = 0
        while right < len(nums):
            diff = nums[right] - nums[left]
            if diff == 1:
                result = max(result, right - left + 1)
            if diff <= 1:
                right += 1
            else:
                left += 1
        return result


s = Solution()
nums = [1, 3, 2, 2, 5, 2, 3, 7]
res = s.findLHS(nums)

print(res)
