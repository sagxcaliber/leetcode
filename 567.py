from typing import *
# not working solution
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         count = 0
#         max_count = 0
#         curr_idx = 0
#         for x in range(len(s2)):
#             if s2[x] in s1:
#                 count += 1
#                 max_count = max(max_count,count)
#                 curr_idx = x
#             else:
#                 count = 0
#                 if curr_idx+1 == x and max_count<=1 and len(s2)>2:
#                     max_count = 0
#         return True if max_count>0 else False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_map = {}
        count_req = len(s1)
        left = 0
        for x in s1:
            if x in hash_map:
                hash_map[x] += 1
            else:
                hash_map[x] = 1

        for right in range(len(s2)):
            print(s2[right],'right')
            print(s2[left],'left')
            if s2[right] in hash_map and hash_map[s2[right]] >0:
                count_req -= 1

            if s2[right] in hash_map:
                hash_map[s2[right]] -= 1

            if right - left + 1 == len(s1) and count_req != 0:
                if s2[left] in s1 and hash_map[s2[left]] > 0:
                    count_req += 1
                if s2[left] in hash_map:
                    hash_map[s2[left]] += 1
                left += 1

            if count_req == 0:
                return True
#
#         return False
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        s1_list = [0] * 26
        s2_list = [0] * 26
        for x in s1:
            idx = ord(x) - ord('a')
            s1_list[idx] += 1

        for right in range(len(s2)):
            current_idx = ord(s2[right]) - ord('a')
            s2_list[current_idx] += 1

            if right-left +1 >len(s1):
                losing_idx = ord(s2[left]) -ord('a')
                s2_list[losing_idx] -=1
                left += 1

            if s1_list ==   s2_list:
                return True

        return False

# {'a':}
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_map = {}
        count_req = len(s1)
        left = 0
        for x in s1:
            if x in hash_map:
                hash_map[x] += 1
            else:
                hash_map[x] = 1

        for right in range(len(s2)):

            if s2[right] in hash_map:
                hash_map[s2[right]] -= 1
                count_req -= 1

            if count_req == 0:
                return True

            if right - left + 1 == len(s1):
                if s2[left] in s1:
                    count_req += 1

                if s2[left] in s1:
                    hash_map[s2[left]] += 1
                left += 1

            if count_req == 0:
                return True

        return False



s=Solution()
s1="ab"
s2="eidbaooo"
# s2="eidbaooo"
# s2="eidboaoo"
res= s.checkInclusion(s1=s1,s2=s2)
print(res)