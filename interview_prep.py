l = [2, 5, 4, 3, 22, 29, -1, 0]
even_list = []
odd_list = []

# need to give 2 list [[even list],[odd list]]
#
# for x in l:
#
#     if x % 2 ==1:
#         odd_list.append(x)
#     else:
#         even_list.append(x)
#
# print([even_list,odd_list])

l1 = [2, 4, 6, 8, 8, 8]
l2 = [4, 8, 12, 8, 36]

l9 = set(l1) - set(l2)
l0 = set(l2) - set(l1)
l11 = list(l9) + list(l0)
print('non in', l11)

s3 = l1 + l2
s1 = set(s3)

s4 = set(l1)
s2 = set(l2)

# for union
l3 = list(s1)
print('union', l3)

l8 = []
# intersaction

for x in l1:
    if x in l2:
        l8.append(x)

s5 = s2 - s1

print('intersation', l8)

s = 'sagar'

l = [1, 2, 3]


def backtrack(l):
    prev = [False] * len(l)
    idx = 0
    ans = []
    temp = [0] * len(l)

    def myfunc(l, idx, prev, temp):

        for i in range(len(l)):
            if idx == len(l):
                ans.append(temp[:])
                return

            else:

                if not prev[i]:
                    prev[i] = True
                    temp[idx] = l[i]

                    myfunc(l, idx + 1, prev, temp)
                    prev[i] = False
                    temp[idx] = 0

    myfunc(l, idx, prev, temp)
    return ans
#
# res = backtrack([1,2,3])
# print(res)

l = [5,4,1,2,3,4,9,-10,11]

sec = float('-inf')
first = float('-inf')

for val in l:

    if val > first:
        sec = first
        first = val
    if first > val > sec:
        sec = val



# print(sec)/

l = [-10,5,4,3,1]

for x in range(len(l)):
    for y in range(len(l)):
        if  l[x] > l[y]:
            l[x],l[y] = l[y],l[x]

print(l)
print(l[2])









