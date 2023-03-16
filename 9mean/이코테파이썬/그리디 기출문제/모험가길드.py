Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=int(input())
human=list(map(int,input().split()))
human.sort()
res=0
#공포도
i=human[0]
idx=0
#가리키는 인덱스 값이 n이상이 되면 종료
while idx<n:
  #가리키는 인덱스 값에 공포도를 더하고 -1을 한 인덱스가 n범위 안에 있고 그 인덱스의 공포도가 i이하면 그룹 결성 가능
  if idx+i-1<n and human[idx+i-1]<=i:
    res+=1
    #갱신될 idx가 n을 넘어가면 다음 반복문은 실패
    if idx+i>=n:
      break
    i=human[idx+i]
    idx=idx+i
  #결성 못하면 break
  else:
    break
print(res)
