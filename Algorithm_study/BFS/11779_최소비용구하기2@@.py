# https://www.acmicpc.net/problem/11779

# from sys import stdin 
# input = stdin.readline
# from heapq import heappop, heappush

# n = int(input())
# m = int(input())
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     a,b,cost = map(int, input().split())
#     graph[a].append((b,cost))
# start, end = map(int, input().split())

# dist = [1e9]*(n+1)    # 1000001 은 틀림
# h = []
# near = [start] *(n+1) ####

# def d():
#     heappush(h, (0, start))
#     dist[start] = 0

#     while h:
#         sum_d, now = heappop(h)
#         if dist[now] < sum_d:
#             continue
#         for next, next_d in graph[now]:
#             cost = sum_d + next_d
#             if cost < dist[next]:
#                 dist[next] = cost
#                 near[next] = now    ####
#                 heappush(h, (cost, next))

# d()
# print(dist[end])


# road = []
# tmp = end
# while tmp != start:
#     road.append(str(tmp))
#     tmp = near[tmp]

# road.append(str(start))
# road.reverse()

# print(len(road))
# print(" ".join(road))


# 현재노드가 아니라 힙에 다음노드를 저장함

from sys import stdin 
input = stdin.readline
from heapq import heappop, heappush

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,cost = map(int, input().split())
    graph[a].append((b,cost))
    
start, end = map(int, input().split())

dist = [1e9]*(n+1)
h = []

def d():
    heappush(h, (0, start, [start]))
    dist[start] = 0

    while h:
        sum_d, now, path = heappop(h)
        if dist[now] < sum_d:
            continue
        if now == end:
            print(dist[end], len(path), sep="\n")
            print(*path)
            break

        for next, next_d in graph[now]:
            cost = sum_d + next_d
            if cost < dist[next]:
                dist[next] = cost
                heappush(h, (cost, next, path+[next]))  ####
 
d()