# https://www.acmicpc.net/problem/2075

from sys import stdin 
input = stdin.readline
import heapq

n = int(input())
h = []

for _ in range(n):  # 우선순위큐를 이용해 큐의 길이를 n만큼 유지한다
    nums = list(map(int,input().split()))

    if not h: 
        for num in nums:
            heapq.heappush(h,num)
    else:
        for num in nums:
            if h[0] < num:              # h[0]보다 큰 숫자면, push
                heapq.heappush(h,num)
                heapq.heappop(h)        # h[0]는 pop
                
print(h[0])