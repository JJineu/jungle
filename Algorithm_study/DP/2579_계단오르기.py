# https://www.acmicpc.net/problem/2579

from sys import stdin
input = stdin.readline

n = int(input())
step = [0] + list(int(input()) for _ in range(n)) 

if n == 1:
    print(step[1])
else:
    dp = [0]*(n+1)
    dp[1] = step[1]
    dp[2] = step[1]+step[2]

    for i in range(3,n+1): 
        dp[i] = max(dp[i-2] + step[i] , dp[i-3] + step[i] + step[i-1])

    print(dp[-1]) 

