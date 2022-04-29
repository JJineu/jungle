# https://www.acmicpc.net/problem/3055

# from sys import stdin 
# input = stdin.readline
# from collections import deque

# R,C = map(int, input().split())
# tmap = [list(input()) for _ in range(R)]
# visit = [[False]*C for _ in range(R)]

# sonic = deque([])
# water = deque([])
# count = 0

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# # 물, 고슴도치 좌표 queue에 추가, visit = True로 설정
# for i in range(R):
#     for j in range(C):
#         if tmap[i][j] == '*':
#             water.append([i,j])
#             visit[i][j] = True
#         elif tmap[i][j] == 'S':
#             sonic.append([i,j])
#             visit[i][j] = True
#         elif tmap[i][j] == 'X':
#             visit[i][j] = True

# # 고슴도치가 이동할 때마다 반복하기
# while sonic:
#     # 물이 찰 예정이면 고슴도치가 이동하지 못하므로, 물 확장부터 구현
#     for _ in range(len(water)):
#         w_x, w_y = water.popleft()
#         for i in range(4):
#             nx = w_x + dx[i]
#             ny = w_y + dy[i]
#             if 0<=nx<R and 0<=ny<C and tmap[nx][ny] == '.': 
#                 water.append((nx,ny))
#                 tmap[nx][ny] = '*'
#                 visit[nx][ny] = True
#     count += 1
#     # 고슴도치 이동 구현
#     for _ in range(len(sonic)):
#         s_x, s_y = sonic.popleft()
#         for i in range(4):
#             nx = s_x + dx[i]
#             ny = s_y + dy[i]
#             if 0<=nx<R and 0<=ny<C:
#                 if tmap[nx][ny] == '.' and visit[nx][ny] == False:
#                     sonic.append((nx,ny))
#                     visit[nx][ny] =True
#                 elif tmap[nx][ny] == 'D':
#                     print(count)
#                     exit()
# print('KAKTUS')



# 큐 하나만들기

input = __import__('sys').stdin.readline
from collections import deque

def bfs():
    while q:
        x, y = q.popleft()
        if graph[xx][yy] == 'S':
            # S 가 D에 도착하면
            return dist[xx][yy]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<r and 0<=ny<c:
                if (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and graph[x][y] == 'S':
                    graph[nx][ny] = 'S'
                    dist[nx][ny] = dist[x][y]+1
                    q.append((nx,ny))
                elif (graph[nx][ny] == '.' or graph[nx][ny] == 'S') and graph[x][y] == '*':
                    graph[nx][ny] = '*'
                    q.append((nx,ny))
    return 'KAKTUS'

r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
dx,dy = [-1,1,0,0],[0,0,-1,1]
dist = [[0]*c for _ in range(r)]
q = deque()
# 고슴도치 S, 동굴 D
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            q.append((i,j))
        elif graph[i][j] == 'D':
            xx, yy = (i,j)
            
# 물 *
for i in range(r):
    for j in range(c):
        if graph[i][j] == '*':
            q.append((i,j))

print(bfs())