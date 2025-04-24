from typing import *


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        hash_map = {0: 1}
        result = 0
        oddCount = 0

        for x in range(len(nums)):

            if nums[x] % 2 == 1:
                oddCount += 1

            if oddCount == k :
                result += hash_map.get(oddCount-k,0)

            hash_map[oddCount] = hash_map.get(oddCount, 0) + 1
            print(hash_map)
        return result


s=Solution()
# r= s.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2],2)
r= s.numberOfSubarrays([1,1,2,1,1,],3)
print(r)