# https://www.acmicpc.net/problem/2206
 
# from sys import stdin
# input = stdin.readline
# from heapq import heappop,heappush

# n, m = map(int, input().split())
# Map = []
# for _ in range(n):
#     Map.append(list(map(int, input().rstrip())))

# def d():
#     h=[]
#     dx = [-1,1,0,0]
#     dy = [0,0,-1,1]
#     heappush(h,(0,0,0,0))
#     while h:
#         a,b,x,y = heappop(h)
#         if x == n-1 and y == m-1:
#             print(a+1)
#             exit()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<n and 0<=ny<m and Map[nx][ny] != -1:
#                 if Map[nx][ny] == 0:
#                     Map[nx][ny] = -1
#                     heappush(h, (a+1,b,nx,ny))
#                 elif Map[nx][ny] == 1:
#                     if b < 1:
#                         Map[nx][ny] = -2
#                         heappush(h, (a+1,b+1,nx,ny))
    
# d()
# print(-1)



# 3차원 사용

from collections import deque

n, m = map(int, input().split())
graph = []

# 3차원 행렬을 통해 벽의 파괴를 파악함. visited[x][y][0]은 벽 파괴 가능. [x][y][1]은 불가능.
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))
    cnt = 0
    while queue:
        a, b, c = queue.popleft()
    
        if a == n - 1 and b == m - 1:
            return visited[a][b][c]

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 다음 이동할 곳이 벽이고, 벽파괴기회를 사용하지 않은 경우
            if graph[nx][ny] == 1 and c == 0 :
                visited[nx][ny][1] = visited[a][b][0] + 1
                queue.append((nx, ny, 1))
                # print('wall', (nx, ny, 1))
                # print(cnt)
            # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이면
            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1
                queue.append((nx, ny, c))
                # print((nx, ny, c))
                # print(cnt)
                print(visited)
            cnt += 1
    return -1

print(bfs(0, 0, 0))