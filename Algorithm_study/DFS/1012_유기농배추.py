# https://www.acmicpc.net/problem/1012

from sys import stdin, setrecursionlimit
setrecursionlimit(10000)
input = stdin.readline

def dfs(x,y):       
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                dfs(nx,ny)

t = int(input())
for _ in range(t):
    M, N, k = map(int, input().split())
    matrix = [[0]*M for _ in range(N)]
    count = 0

    for _ in range(k):
        m, n = map(int, input().split())
        matrix[n][m] = 1

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                dfs(i,j)
                count += 1

    print(count)