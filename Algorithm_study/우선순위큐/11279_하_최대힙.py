# https://www.acmicpc.net/problem/11279
# 최대 힙

from sys import stdin
from heapq import heappop, heappush
input = stdin.readline

def main():

    n = int(input())
    heap =[]

    for i in range(n):
        cmd = int(input())
        if cmd == 0:
            if heap:
                print(-heappop(heap)) # heap에 음수로 저장되어 있으므로, 출력할 때 *(-1)을 하여 원래 값으로 전환
            else:
                print(0)
        else:
            heappush(heap, -cmd) # 최소힙에서 최대힙으로 전환

main()

