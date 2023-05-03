n,c=map(int,input().split())
house=[]
for _ in range(n):
    house.append(int(input()))
house.sort()


#공유기 설치간격을 이분탐색으로 찾기
start=1
end=house[n-1]-house[0]
res=0

while start<=end:
    mid=(start+end)//2
    cur=house[0]
    cnt=1
    for i in range(1,n):
        if house[i]>=cur+mid:
            cur=house[i]
            cnt+=1
    #공유기 설치한 개수가 c이상이면 설치간격을 더 넓혀도 됨
    if cnt>=c:
        start=mid+1
        res=mid
    #설치간격 더 좁히기
    else:
        end=mid-1
print(res)
