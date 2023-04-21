from collections import deque
from queue import PriorityQueue
n,k=map(int,input().split())

lab=[]
for i in range(n):
    lab.append(list(map(int,input().split())))

s,x,y=map(int,input().split())

dx=[0,0,1,-1]
dy=[1,-1,0,0]
def bfs():
    
    q=PriorityQueue()
    time=0
    for i in range(n):
        for j in range(n):
            if lab[i][j]!=0:
                #처음에 우선순위가 낮은 것부터 큐에 넣고싶어서 우선순위큐에 넣음
                q.put((lab[i][j],(lab[i][j],i,j)))

    #큐의 한 사이클을 잡기 위해서 9999라는 더미 값을 우선순위큐에 넣기
    q.put((9999,(9999,1,1)))
    dq=deque()
    for i in range(q.qsize()):
        qc,qx,qy=q.get()[1]
        dq.append((qc,qx,qy))
    while dq:
        qc,qx,qy=dq.popleft()
        #더미 발견하면 한 사이클 종료를 알림 -> time + 1
        if qc==9999:
            time+=1
            dq.append((9999,1,1))
        #s초가 되면 종료
        if time==s:
            break
        
        for i in range(4):
            nx=qx+dx[i]
            ny=qy+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if lab[nx][ny]==0:
                    #해당 바이러스로 덮어버리기
                    lab[nx][ny]=qc    
                    dq.append((lab[nx][ny],nx,ny))

bfs()
res=lab[x-1][y-1]
print(res)
    
