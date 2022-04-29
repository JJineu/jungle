# https://www.acmicpc.net/problem/18352

# bfs
from collections import deque
from sys import stdin 
input = stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)

distance = [-1]*(N+1)
def bfs(start):
    q = deque([start])
    distance[start] = 0
    while q:
        now = q.popleft()
        for next in graph[now]:
            if distance[next] == -1:
                distance[next] = distance[now] +1
                q.append(next)

bfs(X)

flag = False
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        flag = True
    
if not flag:
    print(-1)


# 다익스트라