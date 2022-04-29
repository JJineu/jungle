# https://www.acmicpc.net/problem/2252

from sys import stdin 
from collections import deque
input = stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
inDegree = [0 for i in range(N+1)]
q = deque()
res = []

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)  # a -> b
    inDegree[b] += 1    # b의 진입차수 +=1

# 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
for i in range(1, N+1):
    if inDegree[i] == 0:
        q.append(i)
# 큐가 빌 때까지 반복
while q:
    tmp = q.popleft()
    res.append(tmp)
    for i in graph[tmp]:
        inDegree[i] -= 1    # 연결된 노드들의 진입차수 -=1
        if inDegree[i] == 0:    # 새롭게 진입차수가 0인 노드를 큐에 삽입
            q.append(i)

print(*res)

