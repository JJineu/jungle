# https://www.acmicpc.net/problem/1417
# 국회의원 선거

# from sys import stdin 
# input = stdin.readline

# n = int(input())
# dasom = int(input())

# if n <=1:
#     print(0)

# else:
#     others = []
#     for i in range(n-1):
#         others.append(int(input()))
    
#     result = 0
#     while max(others) >= dasom:
#         data = others.index(max(others))
#         dasom += 1
#         others[data] -= 1
#         result += 1
# print(result)


# 힙
import heapq

N = int(input())
dasom = int(input())
q = []

for _ in range(N-1):
    n = int(input())
    heapq.heappush(q, -n)   #최대힙

res = 0
while q:
    m = -heapq.heappop(q)
    if dasom > m:
        break
    dasom += 1
    res += 1
    heapq.heappush(q, -(m-1))

print(res)


