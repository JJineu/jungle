# https://www.acmicpc.net/problem/13334
# 철로

from sys import stdin 
import heapq

n = int(input())
locations = [list(map(int, input().split())) for _ in range(n)]
D = int(input())

for location in locations:
    if location[0] > location[1]:
        location[0], location[1] = location[1], location[0]

locations.sort(key=lambda x: x[1])

is_possible = []
index, result = 0, 0
for location in locations:
    # 범위를 설정
    start, end = location[1] - D, location[1]

    # 범위를 벗어난 location이라면 넘어감
    if location[1] - location[0] > D:
        continue

    # 범위 안에 들어오는 경우 push
    if start <= location[0] and location[1] <= end:
        heapq.heappush(is_possible, location)

        # 범위를 벗어나는 값이 생기면 pop
        while is_possible[0][0] < start:
            heapq.heappop(is_possible)
    result = max(result, len(is_possible))

print(result)