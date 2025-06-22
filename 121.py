from typing import *
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_val = float('inf')
        min_idx = float('inf')
        max_profit = float('-inf')

        for idx, x in enumerate(prices):
            for y in range(idx,len(prices)):
                max_profit = max(prices[y]-x,max_profit)

        return max_profit



s= Solution()
res = s.maxProfit([2,4,1])

print(res)