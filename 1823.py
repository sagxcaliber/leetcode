class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ctrl = 5
        new_arr = [True] * n
        count = 0
        def rec(count,ctrl):
            count = count % n
            if new_arr[count] :
                new_arr[count] = False
                count = count + (k-1)
                ctrl -= 1

            if ctrl == 1:
                return count
            return rec(count+(k-1),ctrl)
        return rec(count + (k - 1), ctrl)

s=Solution()
n= 6
k=5
print(s.findTheWinner(n,k))