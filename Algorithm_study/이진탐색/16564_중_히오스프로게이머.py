# https://www.acmicpc.net/problem/16564
# 히오스 프로게이머

# 떡 자르기의 반대

from sys import stdin 
input = stdin.readline

n, k = map(int, input().split())
level = list(int(input()) for _ in range(n))

start = min(level)
end = max(level)+k
result = 0

while start <= end:
    mid = (start+end)//2
    sum = 0

    for i in level:
        if i < mid:
            sum += mid - i
    
    if sum > k:
        end = mid -1
    else:
        start = mid + 1
        result = mid

print(result)