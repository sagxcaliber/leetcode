
def subarraySum(arr , k):
    for idx in range(1, len(arr)):
        arr[idx] = arr[idx - 1] + arr[idx]

    n = len(arr)
    ans = 0
    for idx in range(0, n):
        sm = 0
        for jdx in range(idx, n):
            if idx == 0:
                sm = arr[jdx]
            else:
                sm = arr[jdx] - arr[idx - 1]

            if sm == k:
                ans += 1
    return ans


# nums = [1,1,1]
# k = 2
nums= [1,2,3]
k = 3
r=subarraySum(nums,k)
print(r)