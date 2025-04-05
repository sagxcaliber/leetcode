


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=2:
            return True
        sum = 0
        def rec(sum):

           if sum == n:
               return True

           elif sum > n:
               return False

           return rec(sum*2)

        return rec(2*2)

s = Solution()
n = 2
print(s.isPowerOfTwo(n))



# # make circular list itreation
# h = [1,2,3,4,6,7,8,9]
# import time
# count = 0
# while h:
#     count +=1
#     count = count % len(h)
#     print(int(count))
#     time.sleep(1)
#     # print(h[count])