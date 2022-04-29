# https://www.acmicpc.net/problem/10773
# 제로

from sys import stdin 
input = stdin.readline
from collections import deque

k = int(input())
q = deque([])

for _ in range(k):
    cmd = int(input())
    if cmd == 0:
        q.pop()
    else:
        q.append(cmd)

print(sum(q))

