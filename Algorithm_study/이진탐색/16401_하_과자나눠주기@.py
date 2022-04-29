# https://www.acmicpc.net/problem/16401
# 과자 나눠주기

from sys import stdin 
input = stdin.readline

m, n = map(int, input().split())
width = list(map(int, input().split()))

start = 0
end = max(width)
result = 0

while start <= end:
    mid = (start+end)//2
    sum = 0

    if mid == 0:
        sum = 0
        break

    for w in width:
        if w >= mid:
            sum += w//mid   ### point

    if sum < m:
        end = mid -1
    else:
        result = mid
        start = mid +1

print(result)
