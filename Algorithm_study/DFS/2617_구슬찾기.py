# https://www.acmicpc.net/problem/2617

# dfs+위상정렬

# 주어진 문제중에 작은 구슬들 리스트와 큰 구슬들 리스트를 저장한다.
# 그리고 작은 구슬 리스트를 1부터 N까지, 큰 구슬 리스트를 1부터 N까지 두번 검사한 후,
# count가 (N/2 +1)이상이면 절대로 중간에 올 수 없음을 증명할 수 있다.
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N,M = map(int,input().split())
adj_max=[[] for _ in range(N + 1)]
adj_min=[[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    adj_max[a].append(b)    # [[],[],[1],[],[3,2],[1]]
    adj_min[b].append(a)    # [[],[2,5],[4],[4],[],[]]

def dfs(adj_list, v):
    global cnt
    visited[v] = True           
    for i in adj_list[v]:       
        if not visited[i]:
            cnt += 1
            dfs(adj_list, i)

ans = 0
for i in range(1, N+1):
    visited = [False] * (N+1)   # adj_max와 adj_min리스트의 visit이 겹치지 않음

    cnt = 0
    dfs(adj_max, i)
    if cnt >= (N+1)//2:
        ans += 1

    cnt = 0
    dfs(adj_min, i)
    if cnt >= (N+1)//2:
        ans += 1

print(ans)



# 플로이드와샬

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):  # 입력으로 들어오는 구슬 번호대로 무게 순서를 지켜 관계를 2차원 리스트에 1로 표시
    s, e = map(int, input().split())
    arr[s][e] = 1

# 플로이드 와샬 -> 모든 구슬의 연결관계 표시
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][k] and arr[k][j]:
                arr[i][j] = 1


ans = 0
for i in range(1, N+1):
    left_cnt = 0
    right_cnt = 0
    for j in range(1, N+1):
        if i == j:
            continue
        elif arr[i][j] == 1:    # 현재보다 가벼운 구슬 개수 세기
            right_cnt += 1
        elif arr[j][i] == 1:    # 현재보다 무거운 구슬 개수 세기
            left_cnt += 1
    if right_cnt > N//2 or left_cnt > N//2: # 가볍거나 무거운 개수가 중간값 보다 많으면 될 수가 없다
        ans += 1

print(ans)
