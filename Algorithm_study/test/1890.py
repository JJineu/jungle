# https://www.acmicpc.net/problem/1890

from sys import stdin 
input = stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
visit = [[-1]*n for _ in range(n)]

def dfs(x,y):
    dx = [graph[x][y],0]
    dy = [0,graph[x][y]]

    if x == n-1 and y == n-1:
        return 1
    if visit[x][y] != -1:
        return visit[x][y]

    visit[x][y] = 0
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            visit[x][y] += dfs(nx,ny)

    return visit[x][y]

print(dfs(0,0))
