# from typing import *
# class Solution:
#     def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
#         my_min = nums[0]
#         my_max = nums[0]
#         left = 0
#         count = 0
#         for right in range(len(nums)):
#
#             my_min = min(my_min, nums[right - left + 1])
#             my_max = max(my_max, nums[right - left + 1])
#
#             if my_max > maxK:
#                 break
#             if my_min == minK and my_max == maxK:
#                 count += 1
#
#         return count


from typing import *
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        my_min = nums[0]
        my_max = nums[0]
        left = 0
        count = 0
        for right in range(len(nums)):

            my_min = min(my_min, nums[right - left + 1])
            my_max = max(my_max, nums[right - left + 1])

            if my_max > maxK:
                break
            if my_min == minK and my_max == maxK:
                count += 1

        return count

nums= [1,1,1,1]
minK=1
maxK=1
s=Solution()
res = s.countSubarrays(nums,minK=minK,maxK=maxK)
print(res)