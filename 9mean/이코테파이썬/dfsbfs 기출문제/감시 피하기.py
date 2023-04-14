n=int(input())
board=[]
t=[]
res=1
direction=['up','down','left','right']
for i in range(n):
    board.append(list(input().split()))

for i in range(n):
    for j in range(n):
        if board[i][j]=='T':
            #t에는 선생님들의 좌표가 있다
            t.append((i,j))
            
def dfs(x,y,dir):
    global res
    res=0
    #범위 벗어나거나 장애물 발견하면 종료시
    if x<0 or y<0 or x>n-1 or y>n-1 or board[x][y]=='O':
        return
    #학생 발견하면 res=1로 flag세워서 이번 dfs에서는 학생을 만난걸 표시해서 종
    if board[x][y]=='S':
        res=1
        return
    #각 방향대로 파고 들어가
    if dir=='up':
        dfs(x-1,y,'up')
    if dir=='down':
        dfs(x+1,y,'down')
    if dir=='left':
        dfs(x,y-1,'left')
    if dir=='right':
        dfs(x,y+1,'right')
        
def makeO(cnt):
    global res
    if cnt==3:
        res=0
        #모든 선생님의 좌표로 상하좌우 dfs 실행해서 res가 1이라면 학생발견해서 실패
        #0이면 지금 3개 세운것이 학생 발견 못하게해서 성
        for i in range(len(t)):
            for j in range(4):
                dfs(t[i][0],t[i][1],direction[j])
                if res==1:
                    return
                
        res=0
        return
        
    for i in range(n):
        for j in range(n):
            if board[i][j]=='X':
                #백트래킹으로 o , x 설정하고 풀어
                board[i][j]='O'
                makeO(cnt+1)
                board[i][j]='X'
                if res==0:
                    return
            
makeO(0)

if res==0:
    print("YES")
else:
    print("NO")
