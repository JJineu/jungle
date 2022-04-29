# https://www.acmicpc.net/problem/1260

from sys import stdin
from collections import deque

def dfs(v):
    visited[v] = True
    print(v, end =" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end =" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)  # a번째 리스트에 b를 대입
    graph[b].append(a)
for i in range(1, n+1): ####
    graph[i].sort()


visited = [False]*(n+1)
dfs(v)
print()
visited = [False]*(n+1)
bfs(v)
