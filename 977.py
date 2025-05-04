from typing import *
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_array =[0] * (abs(max(nums,key=abs)) + 1)
        final_return = []

        for x in nums:
            new_array[abs(x)] += 1

        for idx,x in enumerate(new_array):
                final_return.extend([idx*idx] * x)
        return final_return

s=Solution()
l = [-4,-1,0,3,10]
res = s.sortedSquares(l)
print(res)