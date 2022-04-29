# https://www.acmicpc.net/problem/17404

INF = float('inf')
N = int(input())
rgb = [list(map(int, input().split())) for _ in range(N)]

ans = INF

for i in range(3):
    dp = [[INF, INF, INF] for _ in range(N)]
    dp[0][i] = rgb[0][i]
    for j in range(1, N):   
        # rgb거리1처럼 dp[j][0]을 더하면 안됨 - 첫번째 행을 해당값 제외하고 초기화 했기때문에, 행이 넘어갈때 구할 수 있는 값이 없음 모든 행이 inf가 되어버림, 
        # range(2,n) 또한 불가 - 모든 dp테이블을 inf로 초기화했기 때문에
        dp[j][0] = rgb[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = rgb[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = rgb[j][2] + min(dp[j-1][0], dp[j-1][1])

    for k in range(3):
        if i != k:
            ans = min(ans, dp[-1][k])

    # for d in dp:
    #     print(*d)
    # print(ans)

print(ans)
