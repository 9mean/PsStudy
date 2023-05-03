n=int(input())
food=list(map(int,input().split()))
d=[0]*(n)
d[0]=food[0]
d[1]=max(food[0],food[1])
for i in range(2,n):
    #직전거를 안먹고 현재먹기 or 현재를 포기하고 직전거를 선택하기
    d[i]=max(d[i-2]+food[i],d[i-1])
print(d[n-1])
