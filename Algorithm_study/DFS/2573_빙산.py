# https://www.acmicpc.net/problem/2573

from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10000)

N, M = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    if iceberg[x][y] == 0:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                iceberg[nx][ny] -= 1
                dfs(nx,ny)

def dfs_div(x,y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M:
            if not visited[x][y]:
                dfs(nx,ny)

year = 0
K = max(iceberg)
while K:
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] > 0:
                dfs(i,j)

    visited = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] > 0:
                dfs_div(i,j)
                year += 1
    K -= 1










