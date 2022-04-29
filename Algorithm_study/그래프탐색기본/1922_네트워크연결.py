# https://www.acmicpc.net/problem/1922
# 최소 스패닝 트리

from sys import stdin 
input = stdin.readline

n = int(input())
m = int(input())
graph = []

for _ in range(m):
    a,b,cost = map(int, input().split())
    graph.append((cost,a,b))
graph.sort()

parent = [0]*(n+1)
for i in range(1,n+1):
    parent[i] = i

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

res = 0
for i in graph:
    cost,a,b = i
    if find(a) != find(b):
        union(a,b)
        res += cost
print(res)