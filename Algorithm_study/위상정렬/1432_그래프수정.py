# https://www.acmicpc.net/problem/1432

# outdegree 사용 -> 간선의 방향 변경 / 최대힙을 사용/ answer를 n부터 대입
# (이름 나이) 이름이 같을때는 나이순으로 -> 우선순위가 낮은 나이 배열 후 이름 배열해야 함
# 따라서 간선의 방향을 바꿔서 뒤는 높은수가 되어야 하기에 최대힙으로 진행, 

import heapq
import sys
input = sys.stdin.readline

def topology_sort():
  q = []
  for i in range(1, n+1):
    if indegree[i] == 0:
      # heapq.heappush(q,i)
      heapq.heappush(q,-i)
  
  N = n
  while q:
    now = -heapq.heappop(q)
    answer[now] = N
    
    for i in node[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        heapq.heappush(q, -i)
    # N+=1
    N -=1

n = int(input())
node = [[] for _ in range((n+1))]
indegree = [0] * (n+1)

# 인접행렬 입력 ->인접리스트로 변경
for v in range(1, n+1):
  temp = [0]+ list(map(int, input().strip()))
  for i in range(1, n+1):
    if temp[i] == 1:        # i -> v
      node[i].append(v)
      indegree[v] += 1

answer = [0]*(n+1)

topology_sort()
if answer.count(0) > 1:
  print(-1)
else:
  print(*answer[1:])