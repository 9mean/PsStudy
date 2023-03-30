# 최소 칸의 개수니까 bfs로
from collections import deque

n,m=map(int,input().split())

count=1 # 총 이동 횟수

maze=[] # 미로 판

move =[(1,0),(-1,0),(0,1),(0,-1)] # 움직일수 있는 방향 (상,하,좌,우)

for i in range(n):
    maze.append(list(map(int,input())))

def bfs(x,y):
    q=deque()
    q.append((x,y)) # 해당 좌표 방문 처리
    while q:
        x,y=q.popleft()
        for i,j in move:
            nx=i+x
            ny=j+y
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if maze[nx][ny]==1:
                    maze[nx][ny]=maze[x][y]+1 # 시작지점의 값은 당연히 1이므로 1바로 옆에 있는 곳은 거리 2 저장.
                    q.append((nx,ny))
  






bfs(0,0)
print(maze[n-1][m-1])
#print(maze)