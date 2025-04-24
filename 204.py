class Solution:
    def countPrimes(self, n: int) -> int:

        count = 0
        for x in range(2, n):
            # 3
            for y in range(2, x):
                if x == 2:
                    count += 1

                if x % y == 0:
                    break
                count += 1
                break

        return count


s=Solution()
res = s.countPrimes(n=3)
print(res)