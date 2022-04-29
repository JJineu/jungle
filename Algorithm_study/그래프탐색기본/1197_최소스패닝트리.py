# https://www.acmicpc.net/problem/1197

# 크루스칼로.
# 낮은 가중치부터 꺼내서 트리를 완성
from sys import stdin
input = stdin.readline

# 경로압축기법
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())

parent = [0]*(v+1)
for i in range(1,v+1):
    parent[i] = i

edges = []
for _ in range(e):
    a,b,cost = map(int, input().split())
    edges.append((cost,a,b))
edges.sort()    # 모든 간선 정렬, 비용순

res = 0
for edge in edges:
    cost, a, b = edge
    # 서로소 집합을 이용한 사이클 판별
    # 사이클이 발생하지 않았으면, 합집합 수행
    if find(a) != find(b):
        union(a,b)
        res += cost

print(res)



# Prim - 다익스트라와 비슷
from sys import stdin
input = stdin.readline
from heapq import heappop, heappush

v, e = map(int, input().split())

edges = [[] for _ in range(v+1)]
for _ in range(e):
    a,b,cost = map(int, input().split())
    edges[a].append((cost, b))
    edges[b].append((cost, a))

visit = [False]*(v+1)
h = [(0, 1)]    # 시작노드 넣어준다

answer = 0
cnt = 0
while h:
    if cnt == v:    # 정점의 개수와 같아지면 break
        break
    cost, x = heappop(h)
    if not visit[x]:
        visit[x] = True
        answer += cost
        cnt += 1
        for i in edges[x]:
            heappush(h, i)
 
print(answer)