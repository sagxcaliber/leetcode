import heapq
from typing import *
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        pq = []
        count = 3
        new_count = 1
        ans = []
        hash_map = {
            3: "Gold Medal",
            2: "Silver Medal",
            1: "Bronze Medal"
        }
        for x in score:
            heapq.heappush(pq, (-x, x))
        for y in score:
            data = heapq.heappop(pq)[1]
            ans.append(hash_map.get(count, str(new_count)))
            count -= 1
            new_count +=1
        return ans

s=Solution()
r=s.findRelativeRanks([5,4,3,2,1])
print(r)


