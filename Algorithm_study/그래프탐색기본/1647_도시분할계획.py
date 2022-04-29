# https://www.acmicpc.net/problem/1647

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

edges = []
for _ in range(m):
    a,b,cost = map(int, input().split())
    edges.append((cost,a,b))
edges.sort()

parent = [0]*(n+1)
for i in range(1,n+1):
    parent[i] = i

res = 0
last = 0
for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a,b)
        res += cost
        last = cost ####

print(res-last)
