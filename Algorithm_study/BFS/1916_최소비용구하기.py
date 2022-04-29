# https://www.acmicpc.net/problem/1916

from heapq import heappop,heappush
from sys import stdin
input = stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,cost = map(int, input().split())
    graph[a].append((b,cost))

Start, End= map(int, input().split())
dist = [10e9]*(N+1)

def dijkstra(start):
    h = []
    heappush(h, (0, start))
    dist[start] = 0         # 시작노드로 가는 최단경로는 0

    while h:
        sum_d, now = heappop(h)
        if dist[now] < sum_d:
            continue
        for next, next_d in graph[now]:    # 현재노드와 인접한 노드 확인
            cost = sum_d + next_d  
            if cost < dist[next]:
                dist[next] = cost
                heappush(h, (cost, next))

dijkstra(Start)
print(dist[End])
