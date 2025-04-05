from typing import *
import re
class Solution:
    def myAtoi(self, s: str) -> int:
        neg = False
        if '-' in s:
            neg = True


        s = re.sub('[^1-9]+',string=s,repl='')
        s = '-' + s[::-1] if neg else s[::-1]
        print(s)
        # re.sub('[^A-Za-z0-9]+', '', s).lower()

s=Solution()
sa = ' -042'
s.myAtoi(sa)