# https://www.acmicpc.net/problem/11725

# 서로소로 푸는것 아님

# dfs
from sys import stdin, setrecursionlimit 
input = stdin.readline
setrecursionlimit(10**9)

n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    

parent = [0]*(n+1)
parent[1] = 1
def dfs(x):
    for i in graph[x]:
        if parent[i] == 0:
            parent[i] = x
            dfs(i)

dfs(1)
print(*parent[2:], sep='\n')



# bfs
from sys import stdin 
input = stdin.readline
from collections import deque

n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    

q = deque()
parent = [0]*(n+1)

def bfs(x):
    q.append(x)
    parent[x] = x
    while q:
        x = q.popleft()
        for i in graph[x]:
            if parent[i] == 0:
                parent[i] = x
                q.append(i)

bfs(1)
print(*parent[2:], sep='\n')
