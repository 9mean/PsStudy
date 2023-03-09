Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #동서남북 방향설정
def setD(d):
  if d==0:
    d=3
  if d==1:
    d=0
  if d==2:
    d=1
  if d==3:
    d=2
  return d

n,m=map(int,input().split())
a,b,d=map(int,input().split())
dx=[0,1,0,0]
dy=[-1,0,1,-1]
board=[list(map(int,input().split())) for _ in range(n)]

#왼쪽으로 돌고 방문+1
d=setD(d)
cnt=1
res=1
while True:
  
  #가고자 하는 방향이 바다거나 방문했다면 왼쪽으로 돌아
  if board[a+dx[d]][b+dy[d]]==1 or board[a+dx[d]][b+dy[d]]==2:
    d=setD(d)
    cnt+=1
  #안가본 곳이면 방문처리후 왼쪽으로 돌아
  else:
    a=a+dx[d]
    b=b+dy[d]
    board[a+dx[d]][b+dy[d]]=2
    res+=1
    d=setD(d)
    cnt=1
  #동서남북 다 돌아봤다면
  if cnt==4:
    #뒤로 한칸가기
    if d==0:
      a,b=a+dx[2],b+dy[2]
    if d==1:
      a,b=a+dx[3],b+dy[3]
    if d==2:
      a,b=a+dx[0],b+dy[0]
    if d==3:
      a,b=a+dx[1],b+dy[1]
    #다시 왼쪽으로 돌기
    d=setD(d)
    cnt=1
    #내가 있는 칸이 바다면 break
    if board[a][b]==1:
      break

print(res)
      
      