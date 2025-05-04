

def get_time(h,m):
    h = h % 12
    min_angle = 6 * m
    hr_angle = 30 * h + 0.5 * m

    total_angle = abs(hr_angle - min_angle)

    print(min(360 - total_angle, total_angle))


# get_time(24,15)



def moveZeros(nums):
    left  = 0
    for right in range(len(nums)):
        if nums[right] == 0 and nums[left] != 0 :
            left = right

        if nums[left] == 0 and nums[right] != 0 :
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
    return nums


nums = [0,1,0]
res = moveZeros(nums)
print(res)