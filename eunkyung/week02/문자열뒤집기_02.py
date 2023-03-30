# 0과 1이 각각 연속된 그룹이 몇개있는지 찾고 그 두개중 가장 적은 그룹의 개수가 답
# idx 0부터 마지막 idx까지 훑으면서 나눠진 그룹별로 count

arr=input()
group1=0
group0=0

now=arr[0] # 가장 첫번째 값
next=''

if now=='0':
    group0+=1
else:
    group1+=1

for i in range(1,len(arr)):
    next=arr[i]
    if now!=next:
        if next=='0':
            group0+=1
        else:
            group1+=1
    now=next
    


# print(group0)
# print(group1)
print(min(group0,group1))

# 성공 !