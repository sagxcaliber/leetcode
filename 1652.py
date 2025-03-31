from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        for x in range(len(code)):
            win_con = code[x] + code[::x+k]


code = [2,4,9,3]
k = -2
s = Solution()
res = s.decrypt(code, k)
# [12,5,6,13]

print(res)
