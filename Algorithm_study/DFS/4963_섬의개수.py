# https://www.acmicpc.net/problem/4963

from sys import stdin, setrecursionlimit
setrecursionlimit(10000)
input = stdin.readline

def dfs(x,y):
    dx = [1,1,1,0,0,-1,-1,-1] # 상 중 하
    dy = [-1,0,1,-1,1,-1,0,1] # 왼 중 오
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<h and 0<=ny<w:
            if land[nx][ny] == 1:
                land[nx][ny] = 0
                dfs(nx,ny)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    land = [list(map(int, input().split())) for _ in range(h)]
    count = 0

    for i in range(h):
        for j in range(w):
            if land[i][j] == 1:
                count +=1
                dfs(i,j)

    print(count)
                


# bfs

from sys import stdin
from collections import deque
input = stdin.readline

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

def bfs(x,y):
    q = deque([])
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<h and 0<=ny<w:
                if land[nx][ny] == 1:
                    land[nx][ny] = 0
                    q.append((nx,ny))


while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    land = [list(map(int, input().split()))  for _ in range(h)]
    count=0

    for row in range(h):
        for col in range(w):
            if land[row][col] == 1:
                land[row][col] = 0
                bfs(row,col)
                count += 1
    print(count)
