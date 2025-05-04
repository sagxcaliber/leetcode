class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = 0
        for right in range(len(nums)):

            if nums[left] != 0 and nums[right] == 0:
                left = right

            if nums[left] == 0 and nums[right] != 0:
                nums[right],nums[left] = nums[left],nums[right]
                left += 1
            print(nums)
        print(nums)

s=Solution()
l=[4,2,4,0,0,3,0,5,1,0]
res=s.moveZeroes(l)
