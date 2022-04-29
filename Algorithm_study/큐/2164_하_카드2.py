# https://www.acmicpc.net/problem/2164
# 카드2

from collections import deque
from sys import stdin 
input = stdin.readline

n = int(input())
q = deque([])

for i in range(n):
    q.append(i+1)

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(*q)