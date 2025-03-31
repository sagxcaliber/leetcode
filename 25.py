from typing import *

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^A-Za-z0-9]+', '', s).lower()
        l = 0
        r = len(s)-1
        while l<r:
            if s[l] ==s[r]:
                pass
                l+=1
                r-=1
            else:
                return False
        return True

s=Solution()

st="A man, a plan, a canal: Panama"
res=s.isPalindrome(s=st)
print(res)