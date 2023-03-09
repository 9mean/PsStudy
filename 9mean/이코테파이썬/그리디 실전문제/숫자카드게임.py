Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n,m=map(int,input().split())
card=[list(map(int,input().split())) for _ in range(n)]
k=0
for i in range(n):
  #각 줄의 최솟값을 K에 저장하여 마지막 줄까지 순회한 결과 가장 큰 K출력
 k=max(k,min(card[i]))
print(k)
  