# https://www.acmicpc.net/problem/2110
# 공유기 설치

# 1. 두 집사이의 거리 for문 중첩 -> 아마 시간초과

# 2. 첫번째 집에 공유기를 놓는다고 생각, 설치 가능한 공유기 개수가 c를 넘어가면 mid+1 else mid-1

from sys import stdin 

n, c = map(int, stdin.readline().split())
li_house = []
for _ in range(n):
    li_house.append(int(stdin.readline()))
li_house.sort()

start = 1                       # 시작값은 최소거리
end = li_house[-1]-li_house[0]  # 끝 값은 최대거리
result = 0 

while start <= end:
    mid = (start + end) // 2        # mid는 인접한 두 집의 최대 거리 구하는 변수
    current = li_house[0]           # 첫번째 집의 좌표를 넣음(첫번째 집에는 무조건 설치)
    count = 1                       # 거리를 재탐색할때마다 count를 초기화해야 하므로

    for i in range(1, len(li_house)):
        if li_house[i] >= current + mid: # (첫번째 집의 좌표 +) 거리 보다 i번째 집의 거리가 같거나 크면, 공유기를 설치. 집의 개수만큼 반복
            current = li_house[i]       # for문이 돌면서 (i번째 집의 좌표 +) 거리를 탐색해야 하므로
            count += 1

    if count >= c:                  # 설치한 공유기가 문제에서 주어진 개수보다 많거나 같을 경우(c는 다 소모되어야 하므로 count가 c보다 많아야 한다.)
        start = mid + 1             # 거리를 늘려 다시 탐색
        result = mid                # 거리값을 결과에 저장
    else:
        end = mid -1                # 설치한 공유기가 적을 경우, 거리를 좁혀 다시 탐색

print(result)