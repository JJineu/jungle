# https://www.acmicpc.net/problem/1939

from collections import deque
from sys import stdin
input = stdin.readline


def bfs(mid):
    q = deque()
    q.append(Start)
    visit = [False]*(n+1)
    visit[Start] = True

    while q:
        now = q.popleft()

        if now == End:
            return True

        for next, next_limit in graph[now]:
            # 방문하지 않은 곳이면서, mid보다 limit이 클때
            if not visit[next] and next_limit >= mid:  
                visit[next] = True
                q.append(next)
    return False


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,limit = map(int, input().split())
    graph[a].append((b,limit))
    graph[b].append((a,limit))

Start, End = map(int,input().split())

min_w, max_w = 1, 1000000000

res = min_w
while min_w <= max_w:
    mid = (min_w + max_w)//2
    if bfs(mid):    # 값이 있으면 = mid 무게로 end를 갈 수 있으면 -> True
        res = mid
        min_w = mid +1
    else:           # 값이 없으면 = mid 무게로 end까지 갈 수 없다. -> False
        max_w = mid -1
print(res)



# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# adj_list = [{} for _ in range(N+1)]
# edges_list = [tuple(map(int, input().split())) for _ in range(M)]
# edges_list.sort(key=lambda x:x[2], reverse=True) # 중량 기준 내림차순

# start, end = map(int, input().split())

# group = list(range(N+1))
# def find_group(node):
#     """node가 속한 그룹 리턴 및 최적화"""
#     if group[node] == node:
#         return node
#     group[node] = find_group(group[node]) 
#     return group[node]

# def union(node_1, node_2):
#     """node_1과 node_2의 그룹을 같은 그룹으로 묶어줌"""
#     group_1 = find_group(node_1) 
#     group_2 = find_group(node_2)
#     if group_1 > group_2: 
#         group_1, group_2 = group_2, group_1
#     group[group_2] = group_1 

# for a, b, weight in edges_list:
#     union(a, b)
#     if find_group(start) == find_group(end): # start랑 end가 이어지면
#         max_weight = weight
#         break

# print(max_weight) 


#
