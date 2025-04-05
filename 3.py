from typing import *


def lengthOfLongestSubstring(s: str) -> int:
    windowStart = 0
    maxWindowSize = 0
    hashMap = {}

    for i in range(len(s)):
        if s[i] in hashMap:
            windowStart = max(windowStart, hashMap[s[i]] + 1)
        hashMap[s[i]] = i
        maxWindowSize = max(maxWindowSize, i - windowStart + 1)
    return maxWindowSize


print(lengthOfLongestSubstring("abcabcbb"))

#
# # s=Solution()
# # st = "abcabcbb"
# # res=s.lengthOfLongestSubstring(st)
#
# # practice code for sliding window
#
# p = [1,2,3,4,5,6,7,8,9,0]
# k = 3
# left = 0
# right = k
#
# max_sum = 0
#
# for x in range(len(p)):
#     sum = 0
#     for y in range(x,right):
#         sum +=p[y]
#     if right <len(p):
#         right += 1
#     print(sum,'left->',x,'<-right',right)
#     max_sum = max(max_sum,sum)
# print(max_sum)
#
#
# def max_profit(prices):
#     n = len(prices)
#     max_profit = 0
#
#     # Iterate over each day as the potential buy day
#     for i in range(n):
#         # For each buy day, iterate over the subsequent days as potential sell days
#         for j in range(i + 1, n):
#             # Calculate the profit
#             profit = prices[j] - prices[i]
#             # Update the maximum profit if the current profit is greater
#             if profit > max_profit:
#                 max_profit = profit
#
#     return max_profit
# print(max_profit([1,2,3,4,5,6,7,8,9,0]))
