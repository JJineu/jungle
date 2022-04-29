from sys import stdin
from collections import deque
input = stdin.readline

def bfs():
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    sec = 0
    while q:
        if sec == S:
            break
        
        for _ in range(len(q)):
            virus, x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny<N and not Map[nx][ny]:
                    Map[nx][ny] = virus
                    q.append((Map[nx][ny],nx,ny))
        sec += 1

N, K = map(int,input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

q = deque()
for i in range(N):
    for j in range(N):
        if Map[i][j]:
            q.append((Map[i][j],i,j))
q = deque(sorted(q))

S, X, Y = map(int, input().split())

bfs()
print(Map[X-1][Y-1])
