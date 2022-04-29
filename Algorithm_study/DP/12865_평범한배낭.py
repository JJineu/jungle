# https://www.acmicpc.net/problem/12865

# from sys import stdin
# input = stdin.readline

# N, K = map(int, input().split())
# knapsack = [[0]*(K+1) for _ in range(N+1)]

# stuff = [[0,0]]
# for _ in range(N):
#     stuff.append(list(map(int, input().split())))


# #냅색 문제 풀이
# for i in range(1, N + 1):
#     for j in range(1, K + 1):
#         weight = stuff[i][0] 
#         value = stuff[i][1]
       
#         if j < weight:
#             knapsack[i][j] = knapsack[i - 1][j] # 물건 무게가 현재 한계무게보다 작으면 위의 값을 그대로 가져온다
#         else:
#             knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

# print(knapsack[N][K])


# 영천
input = __import__('sys').stdin.readline
n, k = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
dp = [0]*(k+1)
for w,v in l:
    for i in range(k, w-1, -1):
        if i<w: 
            break
        dp[i] = max(dp[i], dp[i-w]+v)
        print(dp)
print(dp.pop())
