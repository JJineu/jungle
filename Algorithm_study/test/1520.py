# https://www.acmicpc.net/problem/1520

from sys import stdin,setrecursionlimit
input = stdin.readline
setrecursionlimit(10**6)

m,n = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(m)]
visit = [[-1]*n for _ in range(m)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):

    if x == m-1 and y == n-1:
        return 1
    if visit[x][y] != -1:
        return visit[x][y]

    visit[x][y] = 0
    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y
        if 0<=nx<m and 0<=ny<n:
            if graph[nx][ny] < graph[x][y]:
                visit[x][y] += dfs(nx,ny)
    return visit[x][y]

print(dfs(0,0))
