n=int(input()) # 떠날수 있는 모험가 수
arr=list(map(int,input().split()))

arr.sort() # 오름차순 정렬
group=0 # 전체 그룹수
count=0 # 현재 그룹에 있는 모험가수

for num in arr:
    count+=1 # 현재 그룹에 모험가수
    if count>=num:
        group+=1
        count=0
  

print(group)





