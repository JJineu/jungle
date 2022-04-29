# https://www.acmicpc.net/problem/2667

from sys import stdin 
input = stdin.readline
from collections import deque

n = int(input())
mmap = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque([])
    q.append((x,y))
    mmap[x][y] = 0
    count = 1
    while q: 
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and mmap[nx][ny] == 1:
                mmap[nx][ny] = 0
                q.append((nx,ny))
                count += 1  ####
    return count            ####

res = []
for i in range(n):
    for j in range(n):
        if mmap[i][j] == 1:
            res.append(bfs(i,j))

res.sort()
print(len(res))
print(*res, sep='\n')