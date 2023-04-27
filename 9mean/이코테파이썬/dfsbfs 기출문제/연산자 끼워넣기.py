
n=int(input())
a=list(map(int,input().split()))
op=list(map(int,input().split()))

def dfs(pos,res,plus,minus,multiply,divide):
    global maxRes
    global minRes
    if pos==n:
        maxRes=max(res,maxRes)
        minRes=min(res,minRes)
        return 
    #각 연산자의 개수가 떨어질때까지 dfs 돌려버리기
    if plus:
        dfs(pos+1,res+a[pos],plus-1,minus,multiply,divide)
    if minus:
        dfs(pos+1,res-a[pos],plus,minus-1,multiply,divide)
    if multiply:
        dfs(pos+1,res*a[pos],plus,minus,multiply-1,divide)
    if divide:
        dfs(pos+1,int(res/a[pos]),plus,minus,multiply,divide-1)

maxRes=-123456789
minRes=123456789

dfs(1,a[0],op[0],op[1],op[2],op[3])
        
print(maxRes)
print(minRes)
