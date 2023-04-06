# 0과 1로 묶이는 각각의 그룹 수를 세서 둘중 그룹수가 더 작은 그룹수 값이 답.

arr=list(input())

group_1=0
group_0=0

for i in range(len(arr)-1):
    if arr[i]==arr[i+1]:
        pass
    else:
        if arr[i]=='0':
            group_0+=1
        else:
            group_1+=1

if arr[-1]!=arr[-2]: # 마지막과 그 전이 다르면 위에 식으로 해결이 안됨. 마지막 값과 그전이 다른 경우 예외처리
    if arr[-1]=='0':
        group_0+=1
    else:
        group_1+=1

if group_1==1 or group_0==1: 
    print(1)
else:
    print(min(group_0,group_1))

# -------- 답지 ---------
# data=input()
# count0=0
# count1=0

# if data[0]=='1':
#     count0+=1
# else:
#     count1+=1

# for i in range(len(data)-1):
#     if data[i]!=data[i+1]:
#         if data[i+1]=='1':
#             count0+=1
#         else:
#             count1+=1
            
# print(min(count0,count1))