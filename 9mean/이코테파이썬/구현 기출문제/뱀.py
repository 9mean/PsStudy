Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
#뱀 다시 풀어야
from collections import deque

def setDir(d,dir):
  if dir=='L':
    if d==3:
      d=0
    else:
      d+=1
  if dir=='D':
    if d==0:
      d=3
    else:
      d-=1
  return d
n=int(input())
board=[[0]*(n+2) for _ in range(n+2)]

trick={}
dir=[(1,0),(0,-1),(-1,0),(0,1)]
k=int(input())
for i in range(k):
  a,b=map(int,input().split())
  board[a+1][b+1]=1
l=int(input())
for i in range(l):
  a,b=input().split()
  trick[a]=b
time=0
d=0
board[1][1]=2
q=deque()
q.appendleft((1,1))
hx,hy=1,1
while True:
  time+=1
  if str(time) in trick:
    d=setDir(d,trick[str(time)])
  hx+=dir[d][0]
  hy+=dir[d][1]
  if hx>n or hx<1 or hy>n or hy<1 or board[hx][hy]==2:
    break
  q.appendleft((hx,hy))
  
  if board[hx][hy]==1:
    board[hx][hy]=2
  else:
    board[hx][hy]=2
    k=q.pop()
    board[k[0]][k[1]]=0
print(time)
  