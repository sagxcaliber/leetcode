from typing import *

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1] * len(nums)
        right_product = [1] * len(nums)
        product = 1
        sum_pro = 1
        ans = []
        for x in range(1,len(nums)):
            product = product * nums[ x - 1 ]
            left_product[x] = product

        for y in range(len(nums)-2,-1,-1):
            sum_pro = sum_pro * nums[y + 1]
            left_product[y] *=sum_pro

        # for x in range(len(nums)):
            # outcome = left_product[x] * right_product[x]
            # ans.append(outcome)

        return ans

s=Solution()
l=[1,2,3,4]
r = s.productExceptSelf(l)
print(r)


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [1] * len(nums)

        overall_prod = 1

        for i in range(len(nums)):
            prod[i] = overall_prod
            overall_prod *= nums[i]

        overall_prod = 1
        for j in range(len(nums) - 1, -1, -1):
            prod[j] *= overall_prod
            overall_prod *= nums[j]
        return prod

s=Solution()
l=[1,2,3,4]
r = s.productExceptSelf(l)
print(r)
