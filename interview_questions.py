from itertools import combinations
# need to create sublist  from the list [1,2,3]
#

def my_func(k:list)->list:
    my_final_list = []
    for x in range(len(k)):
        my_final_list.append([k[x]])
        for combo in range(x,len(k)):
            print(k[x],k[combo])
            my_final_list.append([k[x],k[combo]])
    return my_final_list
# res = my_func([1,2,3])


my_list = []
for x in range(1,len([1,2,2])+1):
    for combo in combinations([1,2,3],x):
        my_list.append(list(combo))
# print(my_list)
# print(res)

def all_sublists_backtrack(lst):
    result = []

    def backtrack(start, path):
        # if len(path)==3:
        result.append(path[:])  # add a copy of the current path
        for i in range(start, len(lst)):
            path.append(lst[i])        # choose
            backtrack(i + 1, path)     # explore
            path.pop()                 # un-choose

    backtrack(0, [])
    print(result)
    return result
#
all_sublists_backtrack([1,2,3])


s= 'abcabd'
left = 0
right = 1
min_str = ''
while left < right:
    if s[left] <= s[right]:
        min_str += s[right]
        right+=1
    left +=1
print(min_str)