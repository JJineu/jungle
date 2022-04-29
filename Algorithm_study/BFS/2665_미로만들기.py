# https://www.acmicpc.net/problem/2665

from sys import stdin 
input = stdin.readline
from heapq import heappush, heappop

N = int(input())
maze = []       # 0 검은방(벽)
for _ in range(N):
    maze.append(list(map(int, input().rstrip())))
visited = [[0]*N for _ in range(N)]

def dijkstra():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    h = []
    heappush(h, [0,0,0])
    visited[0][0] = 1
    while h:
        a, x, y = heappop(h)
        if x == N-1 and y == N-1:
            print(a)
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and visited[nx][ny] ==0:
                visited[nx][ny] = 1
                if maze[nx][ny] == 0:   # 벽이 있으면 부수고, 가중치를 더한다
                    heappush(h, [a+1, nx, ny])
                else:
                    heappush(h, [a, nx, ny])


dijkstra()