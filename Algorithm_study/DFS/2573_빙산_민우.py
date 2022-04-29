from collections import deque
from sys import stdin
input = stdin.readline

def check(x, y):
    cnt = 0
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if glacier[nx][ny] == 0:
            cnt += 1
    return cnt

def bfs(x, y):
    visited[x][y] = True
    q = deque([[x, y]])
    while q:
        x, y = q.popleft()
        cnt = check(x, y)
        re[x][y] = (0 if glacier[x][y] - cnt < 0 else glacier[x][y] - cnt)
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and glacier[nx][ny] != 0:
                    visited[nx][ny] = True
                    q.append([nx, ny])
    return

N, M = map(int, input().split())
glacier = [list(map(int, input().split())) for _ in range(N)]
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
answer = 0

while True:
    tmp = 0 # 덩어리 수 
    re = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and glacier[i][j] > 0:
                bfs(i, j)
                tmp += 1
                
    glacier = re

    if tmp == 0:
        print(0)
        break
    if tmp >= 2:
        print(answer)
        break
    answer += 1