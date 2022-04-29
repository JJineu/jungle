# https://www.acmicpc.net/problem/2470
# 두 용액

from sys import stdin 
input = stdin.readline
n = int(input())

n = int(input())
li = list(int(input().split()))
li.sort()

# 이중포인터 설정
left = 0
right = n-1

answer = 2e9
final = []

while left < right: # 인덱스
    l = li[left]
    r = li[right]

    tot = l + r

    if abs(tot) < answer:
        answer = abs(tot)
        final = [l, r]

    if tot < 0:
        left += 1   
    else:
        right -= 1

print(*final)
