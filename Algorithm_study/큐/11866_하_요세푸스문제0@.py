# https://www.acmicpc.net/problem/11866
# 요세푸스 문제 0

from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
q = deque(list(int(i) for i in range(1,n+1)))
circle = []

while q:
    # for i in range(k-1):
    #     q.append(q.popleft())
    # circle.append(q.popleft())    
    q.rotate(-k+1)
    circle.append(q.popleft())
print(f'<{", ".join(map(str, circle))}>')