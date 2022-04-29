# https://www.acmicpc.net/problem/2606

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

N = int(input())
E = int(input())

parent = [0]*(N+1) 
for i in range(1, N+1):
    parent[i] = i

for _ in range(E):
    n,m = map(int, input().split())
    union(n,m)

for i in range(1,N+1):
    find(i)

count = 0
for i in parent[1:]:
    if i == 1:
        count +=1
print(count-1)


# bfs

from sys import stdin
input = stdin.readline
from collections import deque

n = int(input())
e = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [False]*(n+1)
cnt = 0

q = deque([1])
visit[1] = True
while q:
    v = q.popleft()
    for i in graph[v]:
        if not visit[i]:
            visit[i] = True
            q.append(i)
            cnt += 1

print(cnt)



# dfs

from sys import stdin
input = stdin.readline

n = int(input())
e = int(input())
graph = [[] for _ in range(n+1)]

visit = [False]*(n+1)
cnt = 0
def dfs(x):
    global cnt
    visit[x] = True
    for i in graph[x]:
        if not visit[i]:
            cnt += 1
            dfs(i)


for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(cnt)

