from typing import *


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k%2 == 1 and len(nums)<k:
            k=1
            nums[::] = nums[abs(len(nums))-k::] + nums[:abs(len(nums))-k:]
        else:
            nums[::] = nums[abs(len(nums)) - k::] + nums[:abs(len(nums)) - k:]

        print(nums[abs(len(nums)) - k::])
        print(nums[:abs(len(nums)) - k:])

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        print(nums[:k])
        nums[k:] = reversed(nums[k:])
        print(nums[k:])
        print(nums)


s = Solution()
nums = [1,2,3,4,5,6]
res = s.rotate(nums=nums,k=11)

print(res)
