# https://www.acmicpc.net/problem/11053
# 가장 긴 증가하는 부분 수열

from sys import stdin
input = stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1]*N

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))


# 이진탐색

# import bisect

# x = int(input())
# arr = list(map(int, input().split()))

# dp = [arr[0]]

# for i in range(x):
#     if arr[i] > dp[-1]: # 현재 위치(i)가 이전 위치의 원소들보다 크면 dp에 추가한다
#         dp.append(arr[i])

#     else:   # 현재 위치가 이전 위치의 원소보다 작거나 같으면, 
#             # 이전 위치의 원소 중 가장 큰 원소의 index를 구해
#             # dp의 index 원소를 arr[i]로 바꿔준다
#         idx = bisect.bisect_left(dp, arr[i])
#         dp[idx] = arr[i]


# print(len(dp))

