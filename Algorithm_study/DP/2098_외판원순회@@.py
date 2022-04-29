# https://www.acmicpc.net/problem/2098
# https://hongcoding.tistory.com/83

from sys import stdin
input = stdin.readline
INF = float('inf')

def dfs(x, visited):
    if visited == (1 << N) - 1:
        return graph[x][0] if graph[x][0] else INF  # graph[x][0]이 존재하면 = 출발점 0으로 돌아오는 루트가 있다면

    if dp[x][visited] != INF:   # dp 기본식, 계산된 값을 저장해놓음
        return dp[x][visited]

    for i in range(1, N):       # 0번 도시 제외한(출발지), 모든 도시를 탐방
        if not graph[x][i] or visited & (1 << i):   # x -> i(현재도시) 루트가 없거나, 현재도시 방문한 적 있으면
            continue

        dp[x][visited] = min(dp[x][visited], dfs(i, visited|(1<<i)) +graph[x][i] ) 
        # dp[next][nextvisit]이 next도시에서 남은 도시를 거쳐 시작점으로 돌아가는 최소비용이기 때문에
        # dp[cur][visit]은 dp[next][nextvisit]보다 graph[cur][next]만큼의 비용이 더 들 것이다.
    return dp[x][visited]

N = int(input())
dp = [[INF] * (1 << N) for _ in range(N)]
graph = [list(map(int, input().split())) for _ in range(N)]

print(dfs(0, 1))
# for d in dp:
#     print(*d)