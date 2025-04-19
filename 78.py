class Solution:
    def susbset(self,nums):
        res = []
        perm = []
        idx = 0
        def backtrack(nums,perm,idx):

            if idx == len(nums):
                res.append(perm[:])
                return
            perm.append(nums[idx])

            backtrack(nums,perm,idx+1)
            perm.pop()

            backtrack(nums,perm,idx+1)


        backtrack(nums,perm,idx)
        return res

s=Solution()
res = s.susbset([1,2,3])

print(res)