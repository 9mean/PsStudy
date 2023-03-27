Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #입력값 n이 1000이 최대여서 n^2을 한 100만은 1초도 안걸린다
#그래서 단순히 앞에서부터 순서대로 뒤와 비교해가면서 cnt증가
n,m=map(int,input().split())
ball=list(map(int,input().split()))
length=len(ball)
cnt=0
for i in range(length):
  for j in range(i+1,length):
    if ball[i]!=ball[j]:
      cnt+=1

print(cnt)