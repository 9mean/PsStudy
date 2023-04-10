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
    #깊은 복사로 lab 리스트 복사하
    clab=copy.deepcopy(lab)
    for i in range(n):
        for j in range(m):
            #바이러스 큐에 넣기
            if clab[i][j]==2:
                queue.append((i,j))

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m:
                #바이러스 감염시키고 큐에 넣
                if clab[nx][ny]==0:
                    clab[nx][ny]=2
                    queue.append((nx,ny))

    global res
    cnt=0
    #안전영역 개수 세기
    for i in range(n):
        cnt+=clab[i].count(0)
        
    res=max(res,cnt)

def makeWall(cnt):
    if cnt==3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            #백트래킹으로 모든 곳에 벽 세개 두
            if lab[i][j]==0:
                lab[i][j]=1
                makeWall(cnt+1)
                lab[i][j]=0

res=0
makeWall(0)
print(res)
