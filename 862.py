from typing import *

#
# class Solution:
#     def shortestSubarray(self, nums: List[int], k: int) -> int:
#         current_len = float('inf')
#         left = 0
#         start_idx = 0
#         sum_n = 0
#         for right in range(len(nums)):
#             sum_n += nums[right]
#
#             if current_len > right - left + 1 and sum_n >= k:
#                 current_len = right - left + 1
#
#             while sum_n >=k:
#                 start_idx = right
#                 sum_n -= nums[left]
#                 left += 1
#                 current_len = min(current_len,right - left + 1)
#
#
#         return current_len
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        pre_sum = nums[::]

        if k in nums:
            return 1

        for x in range(1, len(nums)):
            pre_sum[x] = nums[x] + pre_sum[x - 1]

            # [84,50,82,112,217]
        left = 0
        current_window_size = float('inf')
        sum_n = 0
        right = len(pre_sum) - 1

        for left in range(len(pre_sum)):
            value = pre_sum[right] - pre_sum[left]
            if value >= k:
                current_window_size = min(current_window_size, right - left + 1)
        return current_window_size if current_window_size != float('inf') else -1
s=Solution()
r=s.shortestSubarray([2,-1,2],3)
print(r)