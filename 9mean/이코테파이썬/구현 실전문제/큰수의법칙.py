Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>n,m,k=map(int,input().split())
num=list(map(int,input().split()))

cnt=0
kcount=0
res=0
#가장 큰 수만 k번 더하면 되기에 리스트 정렬을 먼저 한다
num.sort(reverse=True)

while cnt<m:
  #kcount가 k번 도달하면 가장 큰 수를 더 이상 못쓰기에 두번째 큰수로 한번 쉬어간다. 
  if kcount==k:
    kcount=0
    res+=num[1]
  else:
    res+=num[0]
    kcount+=1
  cnt+=1
print(res)
