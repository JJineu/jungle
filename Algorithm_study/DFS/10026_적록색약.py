# https://www.acmicpc.net/problem/10026

from sys import stdin, setrecursionlimit
setrecursionlimit(10000)
input = stdin.readline


def dfs(arr, x,y):
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    visited[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<N and arr[x][y] == arr[nx][ny]:
            if not visited[nx][ny]:
                visited[nx][ny] = 1
                dfs(arr,nx,ny)

N = int(input().rstrip())
picture = [list(input().rstrip()) for _ in range(N)]
picture_rg =[[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        picture_rg[i][j] = picture[i][j].replace('G','R')


count = 0
visited = [[0]*(N+1) for _ in range(N+1)]
for i in range(N): 
    for j in range(N): 
        if not visited[i][j]:                  
            count +=1 
            dfs(picture,i,j) 

count_rg = 0
visited = [[0]*(N+1) for _ in range(N+1)]
for i in range(N): 
    for j in range(N): 
        if not visited[i][j]: 
            count_rg +=1 
            dfs(picture_rg,i,j)

print(count, count_rg) 

