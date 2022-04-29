# https://www.acmicpc.net/problem/17298

from sys import stdin 
input = stdin.readline

n = int(input())
A = list(map(int, input().split()))
stack = []
NGE = [-1]*n

for i in range(n):  # 인덱스
    while stack and A[stack[-1]] < A[i]:
        NGE[stack.pop()] = A[i]             
    stack.append(i)

print(*NGE)