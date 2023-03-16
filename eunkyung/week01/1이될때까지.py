# 나눌수있으면 나누고 나눌수 없을때 -1

n,m=map(int,input().split())

count = 0 # 몇번 반복했는지 확인하는 변수

while True:
    if n==1:
        break
    if n%m==0:
        n=n//m
        count+=1
    else:
        n=n-1
        count+=1

print(count)

