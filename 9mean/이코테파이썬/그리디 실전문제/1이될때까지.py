n,k=map(int,input().split())
cnt=0
#n이 1이 될때까지 n이 k로 나눠지지 않는다면 n에서 1씩 빼줘서 k로 나눠질 수 있게 해줌
while n!=1:
  if n%k!=0:
    n-=1
    cnt+=1
  else:
    n=n//k
    cnt+=1
print(cnt)
