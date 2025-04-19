class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        final_count = 0
        count = 0
        constent = 'aeiou'
        left = 0
        hash_map = {}
        for right in range(len(s)):
            if s[right] in hash_map and s[right] in constent:
                hash_map[s[right]] += 1
                count += 1
            else:
                if s[right] in constent:
                    hash_map[s[right]] = 1
                    count += 1

            while right - left + 1 > k:
                final_count = max(final_count, count)
                if s[left] in hash_map:
                    hash_map[s[left]] -= 1
                    count -= 1
                left += 1

        final_count = max(final_count, count)
        return final_count

s=Solution()
input  = "abciiidef"
r = s.maxVowels(input,2)
print(r)