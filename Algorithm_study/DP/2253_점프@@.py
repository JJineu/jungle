# https://www.acmicpc.net/problem/2253
# https://velog.io/@grace0st/%EC%A0%90%ED%94%84-%EB%B0%B1%EC%A4%80-2253%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC

from sys import stdin
input = stdin.readline

n, m = map(int,input().split())
dp = list([1e9]*(int((2*n)**0.5)+2) for _ in range(n+1))
dp[1][0] = 0
stones = set([int(input()) for _ in range(m)])

for i in range(2, n+1):
    if i in stones:
        continue
    for j in range(1, int((2*i)**0.5) +1):  # j는 속도, j가 증가했을때의 최댓값(i번 뛰었을때)을 등차수열의 합으로 계산
        dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1])+1    # 마지막 점프의 간격을 뺐을떄의 dp값에 + count 1

answer = min(dp[n])
print(answer if answer != 1e9 else -1)
