# https://www.acmicpc.net/problem/19598

# 참고 https://junbangg.github.io/boj/19598/

from sys import stdin 
input = stdin.readline
import heapq

n = int(input())
con = [list(map(int, input().split())) for _ in range(n)]

con.sort()

h = []

for start, end in con:
    if h and h[0] <= start: # h 존재하고, end값이 start값보다 작을 때,
        heapq.heappop(h)    
    heapq.heappush(h, end)  # end값을 힙에 삽입

print(len(h))