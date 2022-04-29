# https://www.acmicpc.net/problem/13398

from sys import stdin
input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [[0] * N for _ in range(2)]
# dp[0][i] : 특정 원소를 제거하지 않은 경우
# dp[1][i] : 특정 원소를 제거한 경우

dp[0][0] = arr[0] # 1개는 반드시 선택해야 한다.

if N > 1:
    ans = -1e9
    for i in range(1, N):
        # (이전까지의 연속합 + arr[i]) 와 arr[i]를 비교하여 큰 경우를 대입
        dp[0][i] = max(dp[0][i - 1] + arr[i], arr[i])
        # 특정 원소를 제거하는 경우 => 1. i번째 원소를 제거하는 경우 2. i번째 이전에서 이미 특정 원소를 제거하여 i번째 원소를 선택하는 경우
        # 1의 경우 dp[0][i - 1] 2의 경우 dp[1][i-1] + arr[i]
        dp[1][i] = max(dp[0][i - 1], dp[1][i-1] + arr[i])
        # dp 진행 중 가장 큰 값으로 갱신
        ans = max(ans, dp[0][i], dp[1][i])
    print(ans)
else: # N이 1인 경우
    print(dp[0][0])



# dp테이블 2개

t = int(input())
arr = list(map(int, input().split()))
res1 = [i for i in arr]
res2 = [i for i in arr]

for i in range(1, t):
	res1[i] = max(res1[i-1] + arr[i], res1[i])
	res2[i] = max(res2[i-1] + arr[i], res2[i], res1[i-1])

print(max(res2))