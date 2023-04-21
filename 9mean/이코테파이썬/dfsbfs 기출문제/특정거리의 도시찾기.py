#시간초
def dfs(start,length):
    if length>=k:  
        return
    
    for i in street[start]:
        visited[i]=min(visited[i],length+1)
        dfs(i,length+1)
    
n,m,k,x=map(int,input().split())

street=[[] for _ in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    street[a].append(b)
INF=999999999
visited=[INF]*(n+1)
res=[]
visited[x]=0
for i in street[x]:
    visited[i]=1
    dfs(i,1)
for i in range(n+1):
    if visited[i]==k:
        res.append(i)
res.sort()
if len(res)==0:
    print(-1)
else:
    for i in res:
        print(i)
    
        
