# https://www.acmicpc.net/problem/15810
# 풍선 공장
# 이분 탐색/ 우선순위큐

from sys import stdin 
input = stdin.readline

n, m = map(int, input().split())
time = list(map(int, input().split()))

start = 0
end = max(time)*m   # 시간을 최대한 좁혀서 설정
result = 0

while start<=end:
    mid = (start+end)//2
    count = 0

    for staff in time:
        count += mid//staff

    if count < m:
        start = mid + 1
    else:
        result = mid
        end = mid -1

print(int(result))

# 좀더빠른정답
# N, M = map(int, input().split())
# li = list(map(int, input().split()))
# s, e = 0, max(li)*M
# res = 0
# while s <= e:
#     m = (s+e)//2
#     if sum([m//n for n in li]) >= M:
#         res = m
#         e = m-1
#     else:
#         s = m+1
# print(res)