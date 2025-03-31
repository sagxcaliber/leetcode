from typing import *
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prev = strs[0]

        for x in strs[1:]:
            min_size = min(len(prev),len(x))
            lcp = ""
            for y in range(min_size):
                if prev[y] != x[y]:
                    break
                else:
                    lcp += x[y]
            prev = lcp
        return prev

strs= ["flower","flow","flight"]
s=Solution()
res = s.longestCommonPrefix(strs)

print(res)


# todo need to check this again
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        new_strs = strs[0]

        for x in strs[1:]:
            min_len = min(len(new_strs), len(x))
            lcp = ""
            for j in range(min_len):
                if x[j] != new_strs[j]:
                    break
                else:
                    lcp += x[j]

            new_strs = lcp
        return new_strs
