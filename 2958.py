from typing import *
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = 0
        final_count = 0
        left = 0
        hash_map = {}

        for right in range(len(nums)):
            if nums[right] in hash_map:
                if hash_map[nums[right]] < k:
                    hash_map[nums[right]] += 1
                    count += 1
                else:
                    final_count = max(count,final_count)
                    if nums[right] != nums[left]:
                        hash_map[nums[left]] -= 1
                        count -= 1
                        left += 1
            else:
                hash_map[nums[right]] = 1
                count +=1
        return final_count
s=Solution()
r=s.maxSubarrayLength([1,2,3,1,2,3,1,2],2)
print(r)
# count = 5
# final_count =6
# 1:1
# 2:2
# 3:2
# AUCCEERENCE > K:
#  IF NUMS[R]. =NUMS[L]
#     L++
#     R++
# ELSE:
#     FIN = COUNT
#     HASH[L]-=
#     L++
# R++ = L++
