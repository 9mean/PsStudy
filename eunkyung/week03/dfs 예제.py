#DFS 메서드 정의

def dfs(graph,v,visited):
    #현재 노드를 방문 처리
    visited[v]=True
    print(v,end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]: #그중 방문 안된 인접 노드가 있으면
            dfs(graph,i,visited) #dfs 함수 재호출


graph=[[],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]]

visited=[False]*9 #각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)

# 정의된 DFS 함수 호출
dfs(graph,1,visited)

