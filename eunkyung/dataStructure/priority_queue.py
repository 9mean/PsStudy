# 파이썬에서는 코테에서 우선순위 큐를 사용할때 heapq를 사용한다.

import heapq

pq=[]
heapq.heappush(pq,7)
heapq.heappush(pq,10)
heapq.heappush(pq,-4)
heapq.heappush(pq,0)
heapq.heappush(pq,33)

print("size:",len(pq))
while len(pq)>0:
    print(heapq.heappop(pq))
    

