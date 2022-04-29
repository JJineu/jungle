# https://www.acmicpc.net/problem/14888

from sys import stdin
input = stdin.readline

n = int(input())
A = list(map(int, input().split()))
a,b,c,d = map(int, input().split())

min_v = 1e9
max_v = -1e9

def dfs(depth,total,a,b,c,d):
    global min_v, max_v
    if depth == n:
        min_v = min(min_v, total)
        max_v = max(max_v, total)   
        return 
    
    if a:
        dfs(depth+1,total+A[depth],a-1,b,c,d)
    if b:
        dfs(depth+1,total-A[depth],a,b-1,c,d)
    if c:
        dfs(depth+1,total*A[depth],a,b,c-1,d)
    if d:
        dfs(depth+1,int(total/A[depth]),a,b,c,d-1)

dfs(1,A[0],a,b,c,d)
print(max_v)
print(min_v)