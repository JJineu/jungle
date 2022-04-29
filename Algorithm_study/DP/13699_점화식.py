# https://www.acmicpc.net/problem/13699

from sys import stdin
input = stdin.readline

n = int(input())
dp = [0]*(36)
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, n+1): # dp테이블 갱신해주기 위해서 for문을 돌리는건데,
    t = 0
    if i%2:
        for j in range(i//2):       # 길이가 i인 dp테이블을  갱신한다고 보면 된다.
            t += 2*dp[j]*dp[i-j-1]  
        dp[i] = t + dp[i//2]**2
    else:
        for j in range(i//2):
            t += 2*dp[j]*dp[i-j-1]
        dp[i] = t
print(dp[n])