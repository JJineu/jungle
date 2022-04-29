# https://www.acmicpc.net/problem/11279
# 최대 힙

from sys import stdin
import heapq

n = int(stdin.readline())
heap =[]

for i in range(n):
    cmd = int(stdin.readline())
    if cmd == 0:
        if heap:
            print(-1 * heapq.heappop(heap)) # heap에 음수로 저장되어 있으므로, 출력할 때 *(-1)을 하여 원래 값으로 전환
        else:
            print(0)
    else:
        heapq.heappush(heap, -cmd) # 최소힙에서 최대힙으로 전환, 양수값이 클수록 음수값이 커져서 높은 우선순위를 가짐(원래는 수가 작을수록 높은 우선순위)


