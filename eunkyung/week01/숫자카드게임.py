n,m=map(int,input().split()) # 행 , 열
arr = []
for _ in range(n):
    temp =list(map(int,input().split()))
    arr.append(temp)

min_num = []
# 행마다 최솟값 찾기
for i in range(n):
    min_num.append(min(arr[i]))

#print(min_num)

# 그중에 최댓값 찾기
print(max(min_num))



# --------- other solution ---------
min_num=[]
# min, max 사용하지 않고 구현

# min  구현
for i in range(n):
    tmp=10001
    for j in range(m):
        if tmp>arr[i][j]:
            tmp=arr[i][j]
    min_num.append(tmp)

# max 구현
max_num=0
for x in min_num:
    if x>max_num:
        max_num=x

print(max_num)


# ------ 교재 solution -----

n,m=map(int,input().split()) # n,m을 공백으로 구분하여 입력받기

result = 0

# 한줄씩 입력받아 확인
for i in range(n):
    data = list(map(int,input().split()))
    # 현재 줄에서 가장 작은수 찾기
    min_value = min(data)
    # 가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result,min_value)

print(result)


