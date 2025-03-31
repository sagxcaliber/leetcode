from typing import *


#failed test case [3,3]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {x:idx for idx,x in enumerate(nums)}
        print(hash_map)
        left = 0
        right = len(nums)-1
        nums.sort()
        for x in range(1, len(nums)):
            if nums[left] + nums[right] == target:
                return [hash_map[nums[left]],hash_map[nums[right]]]
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1



s=Solution()
arr = [3,2,4]
target = 6
res =  s.twoSum(arr,target)
print(res)


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hash_map = {}
#
#         for idx, x in enumerate(nums):
#             num = target - x
#
#             if num in hash_map:
#                 return [idx, hash_map[num]]
#             else:
#                 hash_map[x] = idx
