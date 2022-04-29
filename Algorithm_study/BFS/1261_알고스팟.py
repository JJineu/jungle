# https://www.acmicpc.net/problem/1261

from sys import stdin
input = stdin.readline
from heapq import heappop, heappush

m, n = map(int, input().split())
maze = []       
for _ in range(n):
    maze.append(list(map(int, input().rstrip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
h = []
visit = [[0]*(m) for _ in range(n)]

def d():
    heappush(h, (0,0,0))
    visit[0][0] = 1
    while h:
        a,x,y = heappop(h)
        if x == n-1 and y == m-1:
            print(a)
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and visit[nx][ny] == 0:
                if maze[nx][ny] == 0:
                    visit[nx][ny] = 1
                    heappush(h, (a, nx,ny))
                else:
                    visit[nx][ny] = 1
                    heappush(h, (a+1, nx,ny))
                    
d()