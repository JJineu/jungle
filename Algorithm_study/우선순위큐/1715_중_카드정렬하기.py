# https://www.acmicpc.net/problem/1715
# 카드 정렬하기

from sys import stdin 
import heapq
input = stdin.readline

n = int(input())
li = []
sum = 0

for _ in range(n):
    heapq.heappush(li, int(input())) # 삽입할 때부터 힙으로 꼭 넣어야 된다

while len(li) > 1:
    card1 = heapq.heappop(li)
    card2 = heapq.heappop(li)
    sum += card1+card2
    heapq.heappush(li, card1+card2)

print(sum)





