# https://www.acmicpc.net/problem/7576

from sys import stdin 
from collections import deque
input = stdin.readline

M,N = map(int, input().split())
box = []
q = deque([])

for i in range(N):
    box.append(list(map(int, input().split())))
    for j in range(M):      # 익은 토마토를 큐에 저장
        if box[i][j] == 1:
            q.append([i,j])

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and box[nx][ny] == 0:
                q.append([nx,ny])
                box[nx][ny] = box[x][y] +1
bfs()
day = 0
for i in box:
    for j in i:
        if j == 0:      # 최단거리를 그래프 모두에 표시한 뒤에도 0이 나오면
            print(-1)   # 안익은 토마토가 존재하므로, -1을 출력한다
            exit(0)     # 0이 존재하지 않으면, 최댓값을 출력해준다.
    day = max(day, max(i))  # box의 행마다 최댓값을 갱신해준다
print(day - 1)          # 처음을 1로 시작했으므로 -1을 한다.