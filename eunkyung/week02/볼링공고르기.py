n,m = map(int,input().split())

ball = list(map(int,input().split()))
count=0

for i in range(1,n):
    for j in range(i+1,n+1):
        if ball[i-1]!=ball[j-1]:
            #print(i,j)
            count+=1


print(count)