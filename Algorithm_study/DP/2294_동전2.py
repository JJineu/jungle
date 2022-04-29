# https://www.acmicpc.net/problem/2294

# DP
from sys import stdin 
from collections import deque
input = stdin.readline

N,K = map(int, input().split())
coin = list(int(input()) for _ in range(N))
d = [10001]*(K+1)
d[0] = 0

for i in coin:
    for j in range(i, K+1):
        if d[j-i] != 10001:
            d[j] = min(d[j], d[j-i]+1)

if d[K] == 10001:
    print(-1)
else:
    print(d[K])


# dfs
# https://alpyrithm.tistory.com/81

# from sys import stdin 
# from collections import deque
# input = stdin.readline

# N,K = map(int, input().split())
# coins = list(int(input()) for _ in range(N))
# visit = [0]*(K+1)
# q = deque()


# for coin in coins:
#     if coin > K:
#         continue
#     q.append([coin, 1])
#     visit[coin] = 1

# flag = True
# while q:
#     val, cnt = q.popleft()
#     if val == K:
#         print(cnt)
#         flag = False
#         break
#     for coin in coins:
#         if val + coin > K:
#             continue
#         if visit[val+coin] == 0:
#             visit[val+coin] = 1
#             q.append([val+coin, cnt+1])

# if flag:
#     print(-1)