from logging.config import stopListening


class Solution:
    def genrate_paranthese(self, n):
        stack = []
        result = []

        def backtrack(openN, closeN):

            if openN == closeN == n:
                result.append(''.join(stack[:]))
                return

            if openN < n :
                stack.append('(')
                backtrack(openN+1, closeN)
                stack.pop()

            if openN > closeN :
                stack.append(')')
                backtrack(openN,closeN+1)
                stack.pop()

        backtrack(0,0,)
        return result

s = Solution()
r = s.genrate_paranthese(n=3)
print(r)
