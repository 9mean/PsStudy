
n,m=map(int,input().split())

ice =[]
visited=[[False]*m for _ in range(n)] # 방문을 했는지 확인하는 리스트 (n행 m열)

for i in range(n):
     ice.append(list(map(int,input())))

move =[(1,0),(-1,0),(0,1),(0,-1)] # 움직일수 있는 방향 (상,하,좌,우)
#dfs
def bfs(x,y):
    visited[x][y]=True # 해당 위치는 방문 처리
    for i,j in move:
        nx=x+i
        ny=y+j
        if nx>=0 and nx<n and ny>=0 and ny<m: #행렬의 범위를 벗어나지 않는지 확인
            if visited[nx][ny]==False and ice[nx][ny]==0:
                bfs(nx,ny)


count=0
for x in range(n):
    for y in range(m):
        if ice[x][y]==0 and visited[x][y]==False:
            bfs(x,y)
            count+=1


print(count)



