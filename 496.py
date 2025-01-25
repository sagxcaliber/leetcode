nums1 = [2,1,3]
nums2 = [2,3,1]
result = []
r = -1
hash_map ={ x:idx for idx,x in enumerate(nums2)}
for x in nums1:
    idx = hash_map[x]+1
    if idx == len(nums2):
        result.append(-1)
        continue
    for y in nums2[idx:]:
        if x<y:
            r=y
            break
        elif x==y:
            continue
    result.append(r)
    r=-1


print(result)

