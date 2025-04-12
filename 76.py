class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window_size = 0  # Min length
        count_required = len(t)
        hash_map = {x: 1 for x in t}
        start_idx = 0
        left = 0
        len_s = len(s)

        if len(t) > len_s:
            return ""

        for right in range(len_s):

            if s[right] in hash_map:
                hash_map[s[right]] -= 1
            else:
                hash_map[s[right]] = -1

            if s[right] in t and count_required != 0:
                count_required = -1

            while count_required == 0:
                current_length = right - left + 1

                if current_length < window_size:
                    window_size = current_length
                    start_idx = left

                if hash_map[s[left]] > 0:  # here iam checking before leaving the left  to update the count_required
                    count_required += 1
                left -= 1

                hash_map[s[left]] = +1

        return s[start_idx: start_idx + window_size]


#
# s = Solution()
af = 'aa'
t = 'aa'


# res = s.minWindow(af, t)
# print(res)

############ Working solution ##############
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window_size = float('inf')
        left = 0
        start_idx = 0
        req_counter = len(t)
        len_s = len(s)
        hash_map = {}
        for x in t:
            if hash_map.get(x):
                hash_map[x] +=1
            else:
                hash_map[x] = 1

        if len(t) > len_s:
            return ""

        for right in range(len(s)):

            if s[right] in t and hash_map[s[right]] > 0:
                req_counter -= 1

            if hash_map.get(s[right]):
                hash_map[s[right]] -= 1
            else:
                hash_map[s[right]] = -1

            while req_counter == 0:

                current_window = right - left + 1
                if current_window < window_size:
                    window_size = current_window
                    start_idx = left

                hash_map[s[left]] += 1

                if s[left] in t and hash_map[s[left]] > 0:
                    req_counter += 1

                left += 1
        return   "" if window_size == float('inf') else s[start_idx:start_idx + window_size]
sv = Solution()

res = sv.minWindow(af, t)
print(res)
