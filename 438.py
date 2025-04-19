from typing import *

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        s_list = [0] * 26
        p_list = [0] * 26
        final_ans = []
        for x in s:
            idx = ord(x) - ord('a')
            s_list[idx] += 1

        for right in range(len(p)):
            current_idx = ord(p[right]) - ord('a')
            p_list[current_idx] += 1

            if right-left +1 >len(s):
                losing_idx = ord(p[left]) -ord('a')
                p_list[losing_idx] -=1
                left += 1

            if s_list  ==   p_list:
                final_ans.append(left)

        return final_ans

s = Solution()
res = s.findAnagrams(s='cbaebabacd',p='abc')
print(res)