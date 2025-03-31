# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for x in range(len(numbers)):
#             for j in range(x+1,len(numbers)):
#                 if numbers[x]+numbers[j] == target:
#                     return [x+1,j+1]
#                 else:
#                     pass
from typing import *
def twoSum( numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left +=  1
        return []


res = twoSum(numbers=[3,24,50,79,88,150,345],target=200)
print(res)