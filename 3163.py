#
# class Solution:
#     def compressedString(self, word: str) -> str:
#         comp = ''
#         for i, x in enumerate(word[:]):
#             if x not in comp:
#                 count = 0
#                 while i < len(word) and word[i] == x and count < 9:
#                     count += 1
#                     i += 1
#                 if count > 0:
#                     comp += f"{count}{x}"
#         return comp


class Solution:
    def compressedString(self, word: str):
        word = word +"0"
        count = 0
        left = 0
        comp = ''

        for right in range(len(word)):
            if word[left] != word[right] or count == 9 :
                comp += f"{count}{word[(right-1)]}"
                count = 0
            left = right

            count +=1
        return comp




s = Solution()
res = s.compressedString('aaaaaaaaaabbbb')
print(res)
