
before=[[1,2,3],[4,5,6],[7,8,9]]
n=len(before)
new = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        new[j][n-i-1]=before[i][j]


print(before)
print(new)