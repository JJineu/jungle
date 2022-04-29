# https://www.acmicpc.net/problem/7569

from sys import stdin 
from collections import deque
input = stdin.readline

M,N,H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
q  = deque([])

# for high in range(H):
#     tmp = []
#     for row in range(N):
#         tmp.append(list(map(int, input().split()))) # 토마토 위치 입력받기
#         for col in range(M):
#             if tmp[row][col] == 1:
#                 q.append([row,col,high])  # 익은 토마토를 큐에 저장
#     box.append(tmp)

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                q.append([i,j,k])

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs():
    while q:
        z,x,y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<N and 0<=ny<M and 0<=nz<H and box[nz][nx][ny]==0:
                q.append([nz,nx,ny])
                box[nz][nx][ny] = box[z][x][y]+1

bfs()
day = 0
for i in box:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        day = max(day, max(j))
            # day = max(day, box[i][j][k])
print(day-1)
