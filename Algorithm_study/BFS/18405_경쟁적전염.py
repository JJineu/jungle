# https://www.acmicpc.net/problem/18405

from collections import deque
from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = deque()
for i in range(N):
    for j in range(N):
        if graph[i][j]:
            q.append((graph[i][j],i,j))
q = deque(sorted(q))


def bfs():
    sec = 0
    
    while q:
        if sec == S:
            break
        for _ in range(len(q)):
            virus, x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny<N and graph[nx][ny] == 0:
                    graph[nx][ny] = virus
                    q.append((virus,nx,ny))
        sec += 1

bfs()

print(graph[X-1][Y-1])