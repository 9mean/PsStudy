x=int(input())
d=[0]*(x+1)

d[2]=d[1]+1
d[3]=d[1]+1

for i in range(2,x+1):
    #이전 값에서 +1 한 경우
    d[i]=d[i-1]+1
    #나누어 떨어지는 경우의 +1 or  중에 작은 값
    if i%5==0:
        d[i]=min(d[i],d[i//5]+1)
    if i%3==0:
        d[i]=min(d[i],d[i//3]+1)
    if i%2==0:
        d[i]=min(d[i],d[i//2]+1)

print(d[x])
    
