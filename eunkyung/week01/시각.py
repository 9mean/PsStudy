from operator import contains


n= int(input())

clock=""
count=0
for i in range(n+1):
    for min in range(60):
        for second in range(60):
            clock=str(i)+str(min)+str(second)
            if '3' in clock:
                count+=1

print(count)