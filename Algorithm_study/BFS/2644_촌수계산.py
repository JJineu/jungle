# https://www.acmicpc.net/problem/2644

# 부모-자식 또한 양방향적이다

from sys import stdin
input = stdin.readline
from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

family = [[] for _ in range(n+1)]
q = deque([])
for _ in range(m):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)

dist = [0]*(n+1)
def bfs(x):
    q.append(x)
    while q:
        x = q.popleft()
        for i in family[x]:
            if dist[i] == 0:
                dist[i] = dist[x] + 1
                q.append(i)
bfs(a)
if dist[b] > 0:
    print(dist[b])
else:
    print(-1)