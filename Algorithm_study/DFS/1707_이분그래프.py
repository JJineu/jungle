# https://www.acmicpc.net/problem/1707

from sys import stdin 
input = stdin.readline

def find(p):
    if parent[p] != p:
        parent[p] = find(parent[p])
    return parent[p]

def union_parent(a,b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

k = int(input())

for _ in range(k):
    V, E = map(int, input().split())

    parent = [0]*(V+1)
    for i in range(1, V+1):
        parent[i] = i

    for i in range(E):
        u, v = map(int, input().split())
        union_parent(u,v)

    for i in range(1, V+1):
        find(i)
        
    if len(set(parent))-1 == 2:
        print("YES")
    else:
        print("NO")


# def find(p):
#     if parent[p] != p:
#         parent[p] = find(parent[p])
#     return parent[p]

# def union_parent(a,b):
#     a = find(a)
#     b = find(b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b 

# n = int(input())
# parent = [0]*(n+1)
# for i in range(1, n+1):
#     parent[i] = i

# for _ in range(n-1):
#     a,b = map(int, input().split())
#     union_parent(a,b)
     
# for i in range(1, n+1):
#     find(i)

# for r in parent[1:]:
#     print(i)