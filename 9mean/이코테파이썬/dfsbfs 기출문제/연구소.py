#왜 pypy3에선 통과하고 python3에선 시간초과
from collections import deque
import copy

n,m=map(int,input().split())
lab=[]
for i in range(n):
    lab.append(list(map(int,input().split())))

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs():
    queue=deque()
    clab=copy.deepcopy(lab)
    for i in range(n):
        for j in range(m):
            if clab[i][j]==2:
                queue.append((i,j))

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if clab[nx][ny]==0:
                    clab[nx][ny]=2
                    queue.append((nx,ny))

    global res
    cnt=0
    for i in range(n):
        cnt+=clab[i].count(0)
        
    res=max(res,cnt)

def makeWall(cnt):
    if cnt==3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j]==0:
                lab[i][j]=1
                makeWall(cnt+1)
                lab[i][j]=0

res=0
makeWall(0)
print(res)
