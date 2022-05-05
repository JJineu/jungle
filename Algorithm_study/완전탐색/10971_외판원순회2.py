#외판원순회2/완전탐색
import sys

N = int(input().split())
travel_cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
min_value = sys.maxsize

def dfs_backtracking(start, next, value, visited):
    global min_value

    if len(visited) == N:
        if travel_cost[next][start] !=0:
            min_value = min(min_value, value + travel_cost[next][start])
        return
    for i in range(N):
        if travel_cost[next][i] != 0 and i not in visited and value < min_value:
            visited.append(i)
            dfs_backtracking(start, i, value + cost[next][i], visited)
            visited.pop()

list = [""]*N
lilist = []

for i in list:
    lilist.append(list(map(int, input().split())))

def solve(n,):


if n == N:
    for 

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    def init_list():
        global node_A
        for i in 
        node_A = Node("A")




#해인
import sys

n = int(sys.stdin.readline())

# 2차원 배열 : 각 인덱스는 노드, 그 안의 원소는 다른 노드를 가는 데에 드는 비용
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in sys.stdin.readline().split()])

# minCost는 최소비용을 비교해줘야 하므로 처음엔 무한대로 설정
minCost = float('inf')
visit = [False for _ in range(n)]

def dfs(start, cur, cost):
    global matrix, minCost, visit
    
    if start == cur and visit.count(False) == 0:
        minCost = min(minCost, cost)
    
    # n개의 노드이므로 for i in range(n)
    for i in range(n):
        # 노드 0부터 n-1까지 인접노드를 한바퀴 돎
        if matrix[cur][i] != 0 and visit[i] != True:
            visit[i] = True
            # 상향식 분석으로 봤을 때, cost에 matrix[cur][i]가 계속 쌓임! (누적됨)
            dfs(start, i, cost+matrix[cur][i])
            # 재귀가 끝났을 때 전역변수인 visit[i]를 False로 초기화해둬야 다음 인접노드 돌 때 잘 돎
            visit[i] = False
            # 재귀가 끝나면 다음 코드가 실행되므로 False를 하나씩 실행해주면서 모두 False로 만들어줌!
    
dfs(0, 0, 0)
print(minCost)


#답
import sys

N = int(input()) #도시의 개수
travel_cost = [list(map(int, input().split())) for _ in range(N)]
min_value = sys.maxsize #출력할 최소값 정의


def dfs_backtracking(start, next, value, visited): #시작도시번호,다음도시번호,비용,방문 도시
    global min_value

    if len(visited) == N: #만약 방문한 도시가 입력받은 도시의 개수라면
        if travel_cost[next][start] != 0: #마지막 도시에서 출발 도시로 가는 비용이 0이 아니라면(즉,갈수 있다면)
            min_value = min(min_value, value + travel_cost[next][start]) #더한 값을 저장되어있는 최소값과 비교해서 대입

    for i in range(N): #도시의 개수 만큼 반복문을 돈다.
        #만약 현재 도시에서 갈 수 있는 도시의 비용이 0이 아니고 이미 방문한 도시가 아니며 그 비용값이 저장되어있는 최소값보다 작다면
        if travel_cost[next][i] != 0 and i not in visited and value < min_value: 
            visited.append(i) #그 도시를 방문목록에 추가
            dfs_backtracking(start, i, value + travel_cost[next][i], visited) #그 도시를 방문한다.
            visited.pop() #방문을 완료했다면 방문목록 해제


#도시마다(0~3) 출발점을 지정
for i in range(N):
    dfs_backtracking(i, i, 0, [i])

print(min_value)