# https://www.acmicpc.net/problem/2178

from sys import stdin
input = stdin.readline
from collections import deque


N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int,input().rstrip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque([[x, y]])
    # q = deque([x,y]) 는 고정된 배열이 아니라, x,y=q.popleft() 
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                q.append([nx,ny])

    return maze[N-1][M-1]

print(bfs(0,0))

# deque 연구
# q = deque(['?']) 선언하면서 바로 삽입할때
# q = deque([x,y]) 는 고정된 배열이 아니라, x,y=q.popleft() 
# ?에는 int 불가, str, list, tuple 형태로 넣어야 한다.
# q = deque('ekef')
# x = q.popleft()
# print(x)