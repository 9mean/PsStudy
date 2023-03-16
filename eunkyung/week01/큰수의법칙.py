n,m,k = map(int,input().split())

arr=list(map(int,input().split()))
arr.sort(reverse=True) # 내림차순 정렬
first=arr[0]
second=arr[1]

result=0 #결과값 저장
count=0 # 연속으로 더할수 있는 회수 count

for _ in range(m):
    if count<k:
        result+=first
        count+=1
    else:
        result+=second
        count=0

print(result)

# -------------------------------------
# 교재 sol 1

n,m,k=map(int,input().split()) # N,M,K 를 공백으로 구분하여 입력받기
data = list(map(int,input().split())) # N개의 수를 공백으로 구분하여 입력받기

data.sort() # 입력받은 수들 정렬하기(오름차순)
first=data[n-1] # 가장 큰 수
second = data[n-2] # 두번째로 큰 수

result = 0

while True:
    for i in range(k): # 가장 큰 수를 k번 더하기
        if m==0:
            break
        result+=first
        m-=1 # 더할때 마다 1씩 빼기
    if m==0:
        break
    result+=second
    m-=1

print(result)

# 교재 sol 2
