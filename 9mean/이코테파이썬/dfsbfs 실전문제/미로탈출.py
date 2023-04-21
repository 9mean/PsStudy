from collections import deque
n,m=map(int,input().split())
block=[]
for i in range(n):
    block.append(list(map(int,input())))
q=deque()
q.append((0,0))
dx=[-1,1,0,0]
dy=[0,0,-1,1]

while q:
    x,y=q.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny>=m or nx>=n or ny<0:
            continue
        if block[nx][ny]==0:
            continue
        if block[nx][ny]==1:
            block[nx][ny]=block[x][y]+1
            q.append((nx,ny))

print(block[n-1][m-1])

