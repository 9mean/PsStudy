import heapq

n = int(input())
cards = []
for i in range(n):
    heapq.heappush(cards, int(input()))

res= 0

if len(cards)==1:
    print(res)

else:
    for _ in range(n-1): # 2개씩 꺼내기 떄문에 n-1
        prev = heapq.heappop(cards)
        cur = heapq.heappop(cards)

        res += prev + cur
        heapq.heappush(cards,prev + cur)
    
    print(res)
