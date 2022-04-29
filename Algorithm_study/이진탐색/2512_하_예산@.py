# https://www.acmicpc.net/problem/2512
# 예산

from sys import stdin 
input = stdin.readline

N = int(input())
budget = list(map(int, input().split()))
M = int(input())

start = 0
end = max(budget)
result = 0

while start<=end:
    mid = (start+end)//2
    sum = 0 

    for n in budget:
        if n > mid:
            sum += mid
        else:           ### point
            sum += n

    if sum > M:
        end = mid -1
    else:
        start = mid +1
        result = mid

print(result)   