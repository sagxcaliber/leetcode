class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        sum = 0
        if n <= 0:
            return False
        if n == 3 or n == 1:
            return True

        def rec(sum):
            if sum == n:
                return True
            elif sum > n:
                return False
            return rec(sum * 3)

        return rec(3 * 3)
