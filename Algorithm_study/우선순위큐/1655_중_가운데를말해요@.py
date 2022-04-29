# https://www.acmicpc.net/problem/1655
# 가운데를 말해요

from sys import stdin 
import heapq
input = stdin.readline

n = int(input())
low_num = []    # [0]은 최대값
high_num = []   # [0]은 최소값

for i in range(n):
    cmd = int(input())
    if len(low_num) == len(high_num):
        heapq.heappush(low_num, -cmd)   # 최대힙, [0]이 가장 큰 수
    else:
        heapq.heappush(high_num, cmd)   # 최소힙, [0]이 가장 작은 수 

    if len(low_num) >= 1 and len(high_num) >= 1 and low_num[0]*-1 > high_num[0]:
        r = heapq.heappop(low_num)
        h = heapq.heappop(high_num)

        heapq.heappush(low_num, -h)
        heapq.heappush(high_num, -r)

    print(low_num[0]*-1)