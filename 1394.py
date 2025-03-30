from typing import List
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hash_map={}
        final_key = 0
        for x in arr:
            if x in hash_map:
                hash_map[x] += 1
            else:
                hash_map[x] = 1
        print(hash_map)
        for key ,value in hash_map.items():
            if key == value and final_key<key:
                final_key = key
        return final_key if final_key != 0 else -1

s=Solution()
res=s.findLucky(arr=[4,3,2,2,4,1,3,4,3])
print(res)

