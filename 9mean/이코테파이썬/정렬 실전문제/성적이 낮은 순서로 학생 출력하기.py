n=int(input())
b=list()
for i in range(n):
    elem=input().split()
    b.append((elem[0],elem[1]))

b=sorted(b,key=lambda elem:elem[1])

for x in b:
    print(x[0],end=' ')
