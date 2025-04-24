

import heapq

l = [2,-4,1,3]

pq= []
for x in l:
    heapq.heappush(pq,(-x,x))
k=3
# while k > 1:
#     heapq.heappop(pq)
#     k -=1
# print(heapq.heappop(pq)[1])
print(heapq.heappop(pq))
print(heapq.heappop(pq))
print(heapq.heappop(pq))
print(heapq.heappop(pq))

# from itertools import  permutations
# p = [1,2,3]
# f = p[::]
# for x in range(len(p)):
#     print(list(permutations(p,x)))