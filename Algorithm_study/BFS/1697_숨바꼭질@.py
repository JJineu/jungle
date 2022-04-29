# https://www.acmicpc.net/problem/1697

# from sys import stdin 
# input = stdin.readline
# from collections import deque

# n, k = map(int, input().split())
# road = [0]*(n+1)

# dist = [0]*100001
# def bfs():
#     q = deque()
#     q.append(n)
#     while q:
#         x = q.popleft()
#         if x == k:
#             print(dist[x])
#             break

#         for j in (x-1,x+1,2*x):
#             if 0<=j<=100001 and not dist[j]:
#                 dist[j] = dist[x] + 1
#                 q.append(j)
                
# bfs()

from sys import stdin 
input = stdin.readline
from collections import deque

def bfs(): 
    q = deque() 
    q.append(n) 
    while q: 
        x = q.popleft() 
        if x == k: 
            print(dist[x]) 
            break 
        for j in (x-1,x+1,x*2): 
            if 0<= j <= MAX and not dist[j]: 
                dist[j] = dist[x] +1 
                q.append(j) 
MAX = 100000 
n,k = map(int,input().split()) 
dist = [0] * (MAX+1) 

bfs()
