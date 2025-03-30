class Solution:
    def pivotInteger(self, n: int) -> int:
        numbers = [x for x in range(1, n + 1)]
        print(numbers)
        left_pre = numbers[::]
        right_pre = numbers[::]

        for x in range(1, len(numbers)):
            left_pre[x] = numbers[x] + left_pre[x - 1]
        print(left_pre)

        for x in range(len(numbers)-1, -1, -1):
            if x != len(numbers)-1:
             right_pre[x] = numbers[x] + right_pre[x + 1]
        print(right_pre)

        for x in range(n):
            if right_pre[x]==left_pre[x]:
                return x+1
        else:
            return -1

s = Solution()
n = 8
p = s.pivotInteger(n)
print(p)