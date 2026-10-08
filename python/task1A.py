def dfs(node, graph, visited):
    visited[node] = True
    print(node, end=" ")

    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited)
            
n = int(input()) 
m = int(input()) 
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [False] * (n + 1)

server = int(input())

print("DFS Traversal:")
dfs(server, graph, visited)
