# https://www.acmicpc.net/problem/2156

from sys import stdin
input = stdin.readline

n = int(input())
grape = [0] + list(int(input()) for _ in range(n))
dp = [0]*(n+1)

if n == 1:
    print(grape[1])
else:
    dp[1] = grape[1]
    dp[2] = max(grape[1], grape[1]+grape[2])

    for i in range(3, n+1):
        dp[i] = max(grape[i]+grape[i-1]+dp[i-3], grape[i]+dp[i-2], dp[i-1])
    print(dp[-1])