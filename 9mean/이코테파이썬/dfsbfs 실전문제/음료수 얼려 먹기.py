def dfs(board,x,y):
  if board[x][y]==1 and visited[x][y]==1:
    return
  
  visited[x][y]=1
  for i in range(4):
    a=dx[i]+x
    b=dy[i]+y
    if a>-1 and b>-1 and a<n and b<m and board[a][b]==0 and visited[a][b]==0:
      dfs(board,a,b)
n,m=map(int,input().split())
board=[]
visited=[[0]*m for _ in range(n)]
s=[]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
cnt=0
for i in range(n):
  board.append(list(map(int,input())))
for i in range(n):
  for j in range(m):
    if board[i][j]==0 and visited[i][j]==0:
      dfs(board,i,j)
      cnt+=1
      
print(cnt)
