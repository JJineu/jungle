# https://www.acmicpc.net/problem/1654
# 랜선자르기

from sys import stdin 
input = stdin.readline

k, n = map(int, input().split())
li = list(int(input()) for _ in range(k))

start = 1   # 0으로 하면 안됨, 인덱스[0]는 가능
end = max(li)
result = 0

while start <= end:
    mid = (start + end)//2
    count = 0

    for i in li:
        count += i//mid

    if count < n:
        end = mid -1
    else:
        result = mid
        start = mid +1

print(result)