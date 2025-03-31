from typing import *
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = 0
        max_count = 0
        curr_idx = 0
        for x in range(len(s2)):
            if s2[x] in s1:
                count += 1
                max_count = max(max_count,count)
                curr_idx = x
            else:
                count = 0
                if curr_idx+1 == x and max_count<=1 and len(s2)>2:
                    max_count = 0
        return True if max_count>0 else False


s=Solution()
s1="a"
s2="ab"
# s2="eidbaooo"
# s2="eidboaoo"
res= s.checkInclusion(s1=s1,s2=s2)
print(res)