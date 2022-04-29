# https://www.acmicpc.net/problem/11722

from sys import stdin
input = stdin.readline

n = int(input())
A = list(map(int, input().split()))
d = [1]*(n)

for i in range(n):
    for j in range(i):
        if A[i] < A[j]:
            d[i] = max(d[i],d[j]+1)
print(max(d))