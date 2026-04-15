from collections import deque

n = int(input())

l = [list(map(int, input().split())) for _ in range(n-1)]

answer=[0] * (n+1)
visited=[0] *(n+1)

graph=dict()

for i in range(n+1):
    graph[i] = list()

for x in l:
    graph[x[1]].append(x[0])
    graph[x[0]].append(x[1])


# print(graph[1])
# print(graph[1][0])
# print(graph[1][1])

def bfs(graph, v, visited):
    queue = deque()
    visited[v] = 1
    queue.append(v)

    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if visited[i]==0:
                queue.append(i)
                answer[i]=x
                visited[i]=1
            

bfs(graph,1,visited)

for i in range(2,n+1):
    print(answer[i])
