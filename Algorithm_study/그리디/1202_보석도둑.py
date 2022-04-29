# https://www.acmicpc.net/problem/1202

from sys import stdin
input = stdin.readline
from heapq import heappop,heappush

n, k = map(int, input().split())
jew = []
for _ in range(n):
    heappush(jew, list(map(int, input().split())))

bags = list(int(input()) for _ in range(k))
bags.sort()

answer = 0
tmp_jew = []
for bag in bags:
    while jew and bag >= jew[0][0]:
        heappush(tmp_jew, -heappop(jew)[1]) # max-heap
    if tmp_jew:
        answer -= heappop(tmp_jew)
    elif not jew:
        break
print(answer)