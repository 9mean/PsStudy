n=int(input())
a=list()
for i in range(n):
    a.append(int(input()))

a.sort(reverse=True)
for x in a:
    print(x,end=' ')
