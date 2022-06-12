# https://www.acmicpc.net/problem/2110
# 공유기 설치

# 1. 두 집사이의 거리 for문 중첩 -> 아마 시간초과

# 2. 첫번째 집에 공유기를 놓는다고 생각, 설치 가능한 공유기 개수가 c를 넘어가면 mid+1 else mid-1

from sys import stdin 
input = stdin.readline

n, c = map(int, input().split())
houses = list(int(input()) for _ in range(n))
houses.sort()

start = 1                       # 시작값은 최소거리
end = houses[-1]-houses[0]      # 끝 값은 최대거리
res = 0 

while start <= end:
    mid = (start + end) // 2        # mid는 인접한 두 집의 최대 거리 구하는 변수
    current = houses[0]             # 첫번째 집의 좌표를 넣음(첫번째 집에는 무조건 설치)
    c_count = 1                     # 거리를 재탐색할때마다 count를 초기화해야 하므로

    # 이렇게 하면 가장 작은 값이 나올수밖에 없다. 생각 잘못함
    # for i in range(1,n):
    #     if houses[i] - houses[i-1] >= width:
    #         c_count += 1

    for i in range(1, n):
        if houses[i] >= current + mid:  # (첫번째 집의 좌표 +) 거리 보다 i번째 집의 거리가 같거나 크면, 공유기를 설치. 집의 개수만큼 반복
            current = houses[i]         # for문이 돌면서 (i번째 집의 좌표 +) 거리를 탐색해야 하므로
            c_count += 1

    if c_count >= c:                    # 설치한 공유기가 문제에서 주어진 개수보다 많거나 같을 경우(c는 다 소모되어야 하므로 count가 c보다 많아야 한다.)
        start = mid + 1                 # 거리를 늘려 다시 탐색
        res = mid                       # 거리값을 결과에 저장
    else:
        end = mid -1                    # 설치한 공유기가 적을 경우, 거리를 좁혀 다시 탐색

print(res)