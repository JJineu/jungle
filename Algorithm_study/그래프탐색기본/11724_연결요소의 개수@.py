# https://www.acmicpc.net/problem/11724

# union_find

from sys import stdin
input = stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b


n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 부모 테이블 초기화
parent = [0]*(n+1)
for i in range(1, n+1):
    parent[i] = i


for _ in range(m):
    u, v = map(int, input().split())
    union(u,v)

for i in range(1, n+1):     # 부모노드가 갱신되지 않은 노드들 때문
    find(i)

res = len(set(parent))-1
print(res)


# dfs

from sys import stdin,setrecursionlimit
input = stdin.readline
setrecursionlimit(10000)

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


visit = [False]*(n+1)
def dfs(x):
    visit[x] = True
    for i in graph[x]:
        if not visit[i]:
            dfs(i)

count = 0
for i in range(1, n+1):
    if not visit[i]:
        count += 1
        dfs(i)

print(count)


# bfs

from sys import stdin
input = stdin.readline
from collections import deque

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


visit = [False]*(n+1)
def bfs(x):
    visit[x] = True
    q = deque([x])
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visit[i]:
                q.append(i)
                visit[i] = True

count = 0
for i in range(1, n+1):
    if not visit[i]:
        count += 1
        bfs(i)

print(count)

