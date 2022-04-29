# https://www.acmicpc.net/problem/2637

from collections import deque
from sys import stdin 
input = stdin.readline


N = int(input())
M = int(input())

connect = [[] for _ in range(N+1)]      # 인접리스트 초기화
needs = [[0]*(N+1) for _ in range(N+1)] # 가중치
inDegree = [0]*(N+1)    # 진입차수 초기화

for i in range(M):
    x, y, k = map(int, input().split())
    connect[y].append((x, k))   # y->x
    inDegree[x] += 1            # 진입차수 증가

q = deque()
for i in range(1, N+1):
    if inDegree[i] == 0 :
        q.append(i)

while q:
    now = q.popleft()
    for n, n_need in connect[now]:      # now -> n
        if needs[now].count(0) == N+1:  # 현 제품이 기본부품이면 = 가중치 리스트의 행 개수
            needs[n][now] += n_need
        else:
            for i in range(1, N+1):
                needs[n][i] += needs[now][i]*n_need # 중간부품*중간부품필요개수
        inDegree[n] -= 1 

        if inDegree[n] == 0:
            q.append(n)


for x in enumerate(needs[n]):
    if x[1] > 0:
        print(*x)
print(needs)


